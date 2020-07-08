#Serialの有効化について
RaspberryPIの初期状態ではSerial(Uart)を使用することができません。
そのためSerial Brickを利用するためには幾つかの作業を行う必要があります。

## ライブラリのインストール
FaBoのシリアルBrickを利用するために、ライブラリをインストールする必要があります。
以下のコマンドにより「pyserial」をインストールして下さい。

```shell
$ sudo pip install pyserial
```

## RaspberryPIのバージョン別対応
RaspberryPIのバージョンによって対応が異なりますのでご注意下さい。

### RaspberryPI 2の場合


#### 1.cmdline.txtの編集
```
sudo vi /boot/cmdline.txt
```

##### 
console=tty1の後に「console=serial0,115200」を削除し、保存します。

環境によっては「serial0」ではなく「ttyAMA0」の場合がありますが、同様に削除して下さい。

##### cmdline.txt (変更前)

```
dwc_otg.lpm_enable=0 console=tty1 console=serial0,115200 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait
```

##### cmdline.txt (変更後)

```
dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait
```

#### 2.再起動
cmdline.txtを変更後、再起動して完了です。

```
sudo reboot
```

### RaspberryPI 3の場合
RaspberryPi 3では内蔵されているBluetoothの影響で設定方法が異なります。

※これはRASPBIAN JESSIEのバージョン「May 2016」で確認したものになります。それより後のバージョンでは対応方法が異なる場合がありますのでご注意下さい。


#### 1.config.txtを編集

以下のコマンドによりconfig.txtを開きます。

```
sudo vi /boot/config.txt
```

##### config.txt
最終行に以下の２行を追加して保存します。

```
core_freq=250
dtoverlay=pi3-miniuart-bt
```

#### 2.cmdline.txtの編集
以下のコマンドによりconfig.txtを開きます。

```
sudo vi /boot/cmdline.txt
```

console=tty1の後に「console=serial0,115200」を追加し、保存します。

##### cmdline.txt (変更前)
```
dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait
```

##### cmdline.txt (変更後)
```
dwc_otg.lpm_enable=0 console=tty1 console=serial0,115200 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait
```

#### 3.再起動
２つのファイル変更後、再起動して完了です。

```
sudo reboot
```
