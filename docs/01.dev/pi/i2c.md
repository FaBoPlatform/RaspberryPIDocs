#I2Cの設定

OUT/INシールドとBrickを使う際に、I2Cを有効にする必要があります。

## I2Cを有効にする

```shell
$ sudo raspi-config
```

![](../img/dev/pi/i2c001.png)

![](../img/dev/pi/i2c002.png)

![](../img/dev/pi/i2c003.png)

![](../img/dev/pi/i2c004.png)

## SMBUSにインストール

```shell
$ sudo apt-get install python-smbus
```

## I2C動作確認用のパッケージをインストールします

```shell
$ sudo apt-get install i2c-tools
```

## モジュールが自動起動するように設定します

`/etc/modules`の最後の行に、`i2c-dev'を追加します。

`/etc/modules`
```
i2c-dev
```
再起動します

```shell
$ sudo reboot
```

## 動作確認

I2CのBrickが接続されている場合、次のコマンドでI2Cアドレスが表示されます

```shell
$ sudo i2cdetect -y 1
```
* サンプルで使用している、Pythonモジュールをインストールします

