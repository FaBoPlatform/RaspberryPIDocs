# SPIの設定

OUT/INシールドとBrickを使う際に、SPIを有効にする必要があります。

## SPIを有効にする

```shell
$ sudo raspi-config
```

![](../img/dev/pi/spi001.png)

![](../img/dev/pi/spi002.png)

![](../img/dev/pi/spi003.png)

![](../img/dev/pi/spi004.png)

## SPI開発用のパッケージをインストールします

```shell
$ sudo apt-get install git
$ git clone git://github.com/doceme/py-spidev
$ cd py-spidev
$ sudo python setup.py install
```

