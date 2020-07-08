# #201 3Axis I2C Brick

[](../img/200_i2c/product/201.jpg)
<!--COLORME-->

## Overview
3軸加速度センサーを使用したBrickです。

I2Cで3軸の加速度データを取得することがきます。

## センサー取得データについて
このBrickでは下の図の3軸の値を取得します。

![](../img/200_i2c/docs/201_3axis_docs_001.jpg)

それぞれ矢印の方向に力がかかるとプラス、逆方向ではマイナスとなります。

なお、このBrickを水平に置いた場合、重力がZ軸にかかっている状態となるので、X軸、Y軸が0に近く、Z軸のみ高い値となります。

## 接続
4Pinケーブルで、OUT/INシールドのI2Cコネクタへ接続します。

※4Pinケーブル、各種OUT/INシールド、各種ケースは別売です。

![](../img/200_i2c/connect/201_3axis_connect.jpg)

写真はArduinoでの接続例です。

![](../img/200_i2c/connect/201_connect_with_rasppi.jpg)

写真はRaspberry Piの接続例です。



## ADXL345 Datasheet
| Document |
|:--|
| [ADXL345 Datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.pdf) |

## Register
| I2C Slave Address |
|:-- |
| 0x53 |

## 回路図
![](../img/200_i2c/schematic/201_3axis.png)

## Library

- pipからインストール
```
$ sudo pip install FaBo3Axis_ADXL345
```
- [Library GitHub](https://github.com/FaBoPlatform/FaBo3Axis-ADXL345-Python)
- [Library Document](http://fabo.io/doxygen/FaBo3Axis-ADXL345-Python/)

## Sample Code

I2Cコネクタに接続した3Axis I2C Brickより３軸の加速度情報を取得し、コンソールに出力します。

```python
# coding: utf-8
import FaBo3Axis_ADXL345
import time
import sys

adxl345 = FaBo3Axis_ADXL345.ADXL345()

try:
    while True:
        axes = adxl345.read()
        sys.stdout.write("\rx = %f, y = %f, z = %f" % (axes['x'],  axes['y'], axes['z']))
        sys.stdout.flush()
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
```

import smbusに失敗する場合はraspi-configでI2C有効化してください。

```shell
sudo raspi-config
```

メニューから[7 Advanced Options]>[P5 I2C]を選択して有効化します


## 構成Parts
- Analog Devices ADXL345

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/201_3axis
