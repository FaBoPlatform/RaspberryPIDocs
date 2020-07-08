# SSHの設定

```
$ sudo raspi-config
```

![](../img/dev/pi/ssh001.png)

![](../img/dev/pi/ssh002.png)

![](../img/dev/pi/ssh003.png)

![](../img/dev/pi/ssh004.png)


## IPアドレスを確認

```
$ ifconfig -a
```

IPアドレスをメモ。

## PCから接続

```
$ ssh pi@メモったIPアドレス
```

pass: raspberry


