# ちびファイ2 MZK-UE150N

## 構成図

![](../img/dev/pi/chibi001.png)

USBポートにちびファイ2を接続する事で、eth1として認識される。(Eathernetポートはeth0)。
eth1のinerface設定をし、固定IPを割り振る。

## ネットワーク構成図

![](../img/dev/pi/chibinet001.png)

|デバイス|IP|用途|
|:--|:--|
|ちびファイ2|192.168.111.1|Router/Gatewayとして使用|
|RaspberryPI|192.168.111.100|固定IPを割り振る|


## 固定IP

`/etc/dhcpcd.conf`

```
interface eth1
static ip_address=192.168.111.100/24
static routers=192.168.111.1
```

## ネットワークの再起動

```
$ sudo /etc/init.d/networking restart
```
