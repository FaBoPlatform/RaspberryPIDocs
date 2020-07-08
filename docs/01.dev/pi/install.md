# RASPBIANのインストール

## RasbianをSDにコピー

https://www.raspberrypi.org/downloads/

![](../img/dev/pi/pi002.png)

![](../img/dev/pi/pi003.png)

ダウンロードして、解凍する。

時間があかかる場合は、ミラーサイトからダウンロードする。

Consoleだけでいい場合は、Liteを、GUIが必要な場合は、PIXELをダウンロードする。

[https://www.raspbian.org/RaspbianMirrors](https://www.raspbian.org/RaspbianMirrors)

日本だと、jaistのミラーサイトなどがある。

[http://ftp.jaist.ac.jp/pub/raspberrypi/raspbian/images/](http://ftp.jaist.ac.jp/pub/raspberrypi/raspbian/images/)


MacのTerminalを立ち上げ、SDカードを抜いた状態で、下記コマンドを実行する。

```shell
$ diskutil list
```

![](../img/dev/pi/pi_sd01.png)

今度は、SDカードを指した状態で、下記コマンドを実行する。


```shell
$ diskutil list
```

Disk2が追加されているのを確認する。

![](../img/dev/pi/pi_sd02.png)

Disk2にアクセスするには、Disk2ではなくRdisk2にするとよい。マウント状態を解除するために下記コマンドを実行。

```shell
$ sudo diskutil unmountDisk /dev/rdisk2
```

![](../img/dev/pi/pi_sd03.png)

解答したimgファイルを下記コマンドでSDカードに焼き込む。

```shell
$ sudo dd bs=1m if=~/Downloads/2017-01-11-raspbian-jessie.img  of=/dev/rdisk2
```

![](../img/dev/pi/pi_sd04.png)


