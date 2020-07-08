# Arduino 1.8.x系のインストール

## Arduino IDEの取得

```
$ wget http://downloads.arduino.cc/arduino-1.8.1-linuxarm.tar.xz
```

## Arduino IDEの解凍

```
$ tar xvf arduino-1.8.1-linuxarm.tar.xz
$ sudo mv  arduino-1.8.1 /usr/local
$ cd /usr/local/arduino-1.8.1
$ sudo ./install.sh
```

## シンボリックリンク作成

```
$ cd /usr/bin
$ ln -s /usr/local/arduino-1.8.1/arduino
$ cd ~/
```
## 実行
```
$ arduino
```