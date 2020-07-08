# PIとWifiSpotでネットワーク構築

## USB Wifiドングル

USB WifiドングルをUSBに接続する。

![](../img/dev/pi/zero_wifi001.png)

## USB Wifiモジュールの確認(Raspberry PI側)

```shell
$ ifconfig -a
```

wlan0が有効になっていれば、USB Wifi モジュールは認識されている

![](../img/dev/pi/pi101.png)

## Wifiの情報をメモする

| 項目 | 値 |
| -- | -- |
| ネットワーク名(SSID) | 接続先のSSID |
| パスワード | 接続先のパスワード |

## SSID, PASSの設定(Raspberry PI側)

Wifiスポットを確認する

```shell
$ sudo iwlist wlan0 scan | grep 接続先のSSID
```

例) 

```shell
$ sudo iwlist wlan0 scan | grep fabkura
ESSID:"fabkura-gclue"
ESSID:"fabkura-youkoso"
```

pass_pharaseを追加する。    

```shell    
$ sudo chmod 666 /etc/wpa_supplicant/wpa_supplicant.conf
$ sudo wpa_passphrase '接続先のSSID' '接続先のパスワード' >> /etc/wpa_supplicant/wpa_supplicant.conf
```

'接続先のSSID'と'接続先のパスワード'には、接続したいWifiのSSID名とパスワードをいれる。

また、id_strの項目を追加し、識別できるようにしておく。

`/etc/wpa_supplicant/wpa_supplicant.conf`
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
        ssid="接続先のSSID"
        #psk="接続先のパスワード"
        psk=****************************************************************
        id_str="Wifi1"
}
```

ネットワーク・インターフェースを再起動。

```shell
$ sudo ifdown wlan0
$ sudo ifup wlan0
```

# 接続テスト

```shell
$ ping www.google.com
$ traceroute www.google.com
```