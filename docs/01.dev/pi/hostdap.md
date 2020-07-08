# Hostdap
## USB WifiドングルをAP化

Hostdapを用いてUSB WifiドングルをAP化

## 必要なパッケージのダウンロード

```bash
$ sudo apt-get install hostapd isc-dhcp-server
```

## 設定

以下のファイルは、すべて`sudo vi <ファイル名>`で編集できます。

###  /etc/dhcp/dhcpd.confの編集

`/etc/dhcp/dhcpd.conf`

```shell
# 下記のように先頭に#をつけてコメントアウト
#option domain-name "example.org";
#option domain-name-servers ns1.example.org, ns2.example.org;

# 行頭のコメントアウト（#）をはずす
authoritative;

#最後に追記する
subnet 192.168.42.0 netmask 255.255.255.0 {
range 192.168.42.10 192.168.42.50;
option broadcast-address 192.168.42.255;
option routers 192.168.42.1;
default-lease-time 600;
max-lease-time 7200;
option domain-name "local";
option domain-name-servers 8.8.8.8, 8.8.4.4;
}
```

### /etc/default/isc-dhcp-serverの編集

`/etc/default/isc-dhcp-server`

```shell
INTERFACES=""
```

を、

```shell
INTERFACES="wlan0"
```

に書き換えます。

### /etc/network/interfacesの編集

iface wlan0~ のすぐ下の行、wpa-conf~の行頭に#をつけてコメントアウトします。

`/etc/network/interfaces`

```shell
iface wlan0 inet manual
#    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```
### /etc/dhcpcd.confの編集


最終行に追記します。

`/etc/dhcpcd.conf`


```shell
interface wlan0
static ip_address=192.168.42.1/24
```

### /etc/hostapd/hostapd.confの新規作成

このファイルは存在しないので新たに作ります。


`/etc/hostapd/hostapd.conf`
```
interface=wlan0
driver=nl80211
#driver=rtl871xdrv
ssid=Pi3-AP
hw_mode=g
channel=6
ieee80211n=1
wmm_enabled=1
ht_capab=[HT40][SHORT-GI-20][DSSS_CCK-40]
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_key_mgmt=WPA-PSK
wpa_passphrase=raspberry
rsn_pairwise=CCMP
```

### /etc/default/hostapd の編集

これで、SSID:`Pi3-AP`, PASS:`raspberry`でAP化できるようになります。
下記の記述がコメントアウトされているので行頭の#を削除し、編集します。

`/etc/default/hostapd`

```shell 
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```
### /etc/sysctl.confの編集

下記の行のコメントをはずすだけです。

`/etc/sysctl.conf`
```
net.ipv4.ip_forward=1
```
### /lib/dhcpcd/dhcpcd-hooks/70-ipv4-natの新規作成

このファイルは存在しないので新たに作り、以下の記述をします。

`/lib/dhcpcd/dhcpcd-hooks/70-ipv4-nat`
```
iptables-restore < /etc/iptables.ipv4.nat
```

### iptableへの追加

その後、以下のコマンドを実行してください。

```bash
$ sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"
$ sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
$ sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
$ sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
$ sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
```
ここで、

```
modprobe: ERROR: ../libkmod/libkmod.c:557 kmod_search_moddep() could not open moddep file '/lib/modules/4.4.34-v7+/modules.dep.bin'
iptables v1.4.21: can't initialize iptables table `nat': Table does not exist (do you need to insmod?)
Perhaps iptables or your kernel needs to be upgraded.
```

2つ目のコマンドで、上記のようなエラーメッセージが出た場合、

```bash
$ sudo apt-get dist-upgrade
$ sudo rpi-update
$ sudo reboot # 反映させるために再起動
```
その後にエラーの発生したコマンドから再実行してください。


### 設定が正しいか確認

確認をします。

```bash
$ sudo /usr/sbin/hostapd /etc/hostapd/hostapd.conf
```
これで、プロンプトが返ってこなければ成功です。他の端末などで`Pi3-AP`がWifiとして認識されるか確認してください。
確認したその後は、`Ctrl-c`でプロンプトを返してください。

もし、エラーが出た場合は設定に抜けがないか、タイプミスなどがないか一度ご確認ください。
バージョンの違いでエラーが発生する場合もあります。今回確認したものは、

```shell
Kernel Version : 4.9.13-v7+
hostapd v2.3-1+deb8u4
isc-dhcp-server v4.3.1-6+deb8u2
```

ご自身の環境での各パッケージのバージョンの確認は`apt-cache policy <パッケージ名>`で確認できます。


### サービス開始

以下のコマンドでサービスを開始します

```bash
$ sudo service hostapd start
$ sudo service isc-dhcp-server start
```
さらに、`/etc/init.d/isc-dhcp-server`に以下の記述もします

```
...
start)
test_config
log_daemon_msg "Starting $DESC" "$NAME"
### 以下の場所に追記
sleep 7  
### 以上を追記
start-stop-daemon --start --quiet --pidfile "$DHCPD_PID" \
...
```

IPアドレスは、192.168.42.XXXでアサインされます

### 参考資料:
[http://qiita.com/mt08/items/f2e4f9d3b1ed00849e23#手順](http://qiita.com/mt08/items/f2e4f9d3b1ed00849e23#手順)
