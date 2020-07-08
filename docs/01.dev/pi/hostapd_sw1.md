# hostapdとWifiClientの切り替え

Hostapd起動中は別途USBのWifiアダプタなどを使用しない限りWifiクライアントとして利用できないため、それを簡単に切り替えれるように設定します。

`Hostapd`を利用するために設定したファイルのうち、以下のファイルを編集します。

- `/etc/dhcpcd.conf`
- `/etc/sysctl.conf`
- `/etc/network/interfaces`

今回はこれらのファイルに対し、AP化オン時オフ時それぞれのファイルを作成し、設定に対して上記のファイルを差し替えます。

なお、切り替え時は`~/.ap_mode`ファイルの中身が`1`ならAP化オン、`0`ならAP化オフにし、`sudo reboot`することで設定が反映されるようにします。

### Hostapdオン時の設定ファイルの退避

新しく、`~/`以下に`.ap`ファイルを作成します。
``` bash
$ cd
$ mkdir .ap/
```

その後、`.ap/`ディレクトリに移動し、その中に`on_ap_configfiles/`, `on_wifi_configfiles/`を作成します
``` bash
$ cd ~/.ap
$ mkdir on_ap_configfiles/
$ mkdir on_wifi_configfiles/
```

なお、`~/.ap/on_ap_configfiles/`内に **AP化オン時の設定ファイル**、`~/.ap/on_wifi_configfiles/`内に **AP化オフ時の設定ファイル**を保存します。

**Hostapdの設定を行ってあることが前提** で、次のコマンドを実行し、AP化オン時の設定ファイルをコピーします
``` bash
$ cd ~/.ap/on_ap_configfiles/
$ cp /etc/network/interfaces ./
$ cp /etc/dhcpcd.conf ./
$ cp /etc/sysctl.conf ./
```

- - -

### /etc/dhcpcd.conf ファイルの編集
以下のコマンドで、`dhcpcd.conf`ファイルを`~/.ap/on_wifi_configfiles/`にコピーします
``` bash
$ cd ~/.ap/on_wifi_configfiles/
$ cp ../on_ap_configfiles/dhcpcd.conf ./
```

このコピーしてきた(`~/.ap/on_ap_configfiles/`以下の)ファイルを編集します。

編集方法は簡単で、その他すべての設定ファイルについてもHostapd設定時に変更した点を戻せばいいだけです。

ファイルの末尾に記述した、
``` 
...
interface wlan0
static ip_address=192.168.42.1/24
```
以上の記述を以下のようにコメントアウトします
``` 
...
#interface wlan0
#static ip_address=192.168.42.1/24
```

- - -

### /etc/network/interfaces ファイルの編集
以下のコマンドで、`intefaces`ファイルを`~/.ap/on_wifi_configfiles/`にコピーします
``` bash
$ cd ~/.ap/on_wifi_configfiles/
$ cp ../on_ap_configfiles/interfaces ./
```

このコピーしてきた(`~/.ap/on_ap_configfiles/`以下の)ファイルを編集します。

``` 
...
iface wlan0 inet manual
#   wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
...
```

この記述を、

``` 
...
iface wlan0 inet manual
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
...
```

このように、`wpa_conf ...`という記述のある行のコメントアウトを外します

- - -

### /etc/sysctl.conf ファイルの編集
以下のコマンドで、`sysctl.conf`ファイルを`~/.ap/on_wifi_configfiles/`にコピーします
``` bash
$ cd ~/.ap/on_wifi_configfiles/
$ cp ../on_ap_configfiles/sysctl.conf ./
```

このコピーしてきた(`~/.ap/on_ap_configfiles/`以下の)ファイルを編集します。

``` 
...
net.ipv4.ip_forward=1
...
```

この記述を、

``` 
...
#net.ipv4.ip_forward=1
...
```

コメントアウトします。

- - -

### 自動実行されるスクリプトファイルの作成
この設定を反映させるために、起動時に実行するスクリプトを書きます。

`~/.ap/`以下に`toggle_ap_wifi.sh`ファイルを作成し、ここに以下のスクリプトを記述します。

``` bash
#!/bin/bash

flg=`cat /home/pi/.ap_mode`

oldval=`sysctl net.ipv4.ip_forward | awk 'BEGIN{FS=" "}{print $3}'`

if [ -e /home/pi/.ap_mode -a $flg = '1' ] ; then
    cp /home/pi/.ap/on_ap_configfiles/interfaces   /etc/network/interfaces
    cp /home/pi/.ap/on_ap_configfiles/dhcpcd.conf  /etc/dhcpcd.conf
    cp /home/pi/.ap/on_ap_configfiles/sysctl.conf  /etc/sysctl.conf
else
    cp /home/pi/.ap/on_wifi_configfiles/interfaces   /etc/network/interfaces
    cp /home/pi/.ap/on_wifi_configfiles/dhcpcd.conf  /etc/dhcpcd.conf
    cp /home/pi/.ap/on_wifi_configfiles/sysctl.conf  /etc/sysctl.conf
fi

if [ $flg != $oldval ] ; then
  if [ $flg = '1' ] ; then
    systemctl enable hostapd
    systemctl enable isc-dhcp-server
  else 
    systemctl disable hostapd
    systemctl disable isc-dhcp-server
  fi
  echo 1
  reboot
fi
```

- - -

### ここまでのディレクトリツリー
ここまでのディレクトリツリーを確認します。
以下のようになっていなかったら、再度手順を見直してください
```
- ~/
    - .ap_mode                <- 設定用ファイル(中身は 1 or 0)
    - .ap/
        - toggle_ap_wifi.sh   <- 自動反映用のスクリプト
        - on_ap_configfiles/
            - interfaces      <- AP化オン時の設定のもの
            - sysctl.conf     <- AP化オン時の設定のもの
            - dhcpcd.conf     <- AP化オン時の設定のもの
        - on_wifi_configfiles/
            - interfaces      <- AP化オフ時の設定のもの
            - sysctl.conf     <- AP化オフ時の設定のもの
            - dhcpcd.conf     <- AP化オフ時の設定のもの
```

- - -

### 自動実行されるように設定
`/etc/rc.local`に以下の記述をします
``` bash
...

##### add this code
bash /home/pi/.ap/toggle_ap_wifi.sh
#####

exit 0
```
**注意** : `exit 0`の直前に記述してください

その後、実際に`~/.ap_mode`ファイルを作成し、
```
0
```

ないしは

```
1
```

と記述して、`sudo reboot`し、動作が正しいことを確認してください

- - -

**注意** ) なお、この設定を施したあとに`/etc/network/interfaces`, `/etc/dhcpcd.conf`, `/etc/sysctl.conf`ファイルを変更する際は **`~/.ap/on_ap_configfiles/`,`~/.ap/on_wifi_configfiles/`内のファイルを両方変更してください**

