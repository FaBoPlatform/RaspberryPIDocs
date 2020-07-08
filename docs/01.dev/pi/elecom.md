# ちびファイ MZK-RP150NA

## 構成図

![](../img/dev/pi/elecom001.png)

EthenetポートにWR-583RD2-2を接続することで、IPを割り振る。

## ネットワーク構成図

![](../img/dev/pi/elecomnet001.png)

|デバイス|IP|用途|
|:--|:--|
|WR-583RD2-2|192.168.2.1|Router/Gatewayとして使用|
|RaspberryPI|192.168.2.100|固定IPを割り振る|


## 固定IP

`/etc/dhcpcd.conf`

```
interface eth0
static ip_address=192.168.2.100/24
static routers=192.168.2.1
```

## ネットワークの再起動

```
$ sudo /etc/init.d/network restart
```