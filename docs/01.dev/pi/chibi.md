# ちびファイ MZK-RP150NA

## 構成図

![](../img/dev/pi/chibi002.png)

Ethenetポートにちびファイを接続することで、IPを割り振る。

## ネットワーク構成図

![](../img/dev/pi/chibinet002.png)

|デバイス|IP|用途|
|:--|:--|
|ちびファイ2|192.168.111.1|Router/Gatewayとして使用|
|RaspberryPI|192.168.111.100|固定IPを割り振る|


## 固定IP

`/etc/dhcpcd.conf`

```
interface eth0
static ip_address=192.168.111.100/24
static routers=192.168.111.1
```

## ネットワークの再起動

```
$ sudo /etc/init.d/networking restart
```
