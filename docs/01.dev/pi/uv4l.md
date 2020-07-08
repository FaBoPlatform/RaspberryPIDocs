# UV4L

## パッケージのインストール

`/etc/apt/sources.list`に下記の行を追加する。

```
deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/ jessie main
```

```shell
$ sudo apt-get update
$ sudo apt-get install uv4l uv4l-webrtc uv4l-uvc uv4l-xscreen uv4l-dummy
```

## UVSデバイスを取得

```shell
$ lsusb
```

## 