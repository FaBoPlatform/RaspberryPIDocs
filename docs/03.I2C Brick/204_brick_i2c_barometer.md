# #204 Barometer I2C Brick

[](../img/200_i2c/product/204.jpg)
<!--COLORME-->

## Overview
大気圧センサを使用したBrickです。

I2Cでデータを取得できます。

## 接続
I2Cコネクタへ接続します。

### Arduino
![](../img/200_i2c/connect/204_barometer_connect.jpg)
### Raspberry Pi
![](../img/200_i2c/connect/204_connect_with_rasppi.jpg)

## MPL115A2 Datasheet
| Document |
| -- |
| [MPL115A2 Datasheet](http://cache.freescale.com/files/sensors/doc/data_sheet/MPL115A2.pdf) |

## Register
| Slave Address |
| -- |
| 0x60 |

## 回路図
![](../img/200_i2c/schematic/204_barometer.png)

## Library

- pipからインストール
```
sudo pip install FaBoBarometer_MPL115
```
- [Library GitHub](https://github.com/FaBoPlatform/FaBoBarometer-MPL115-Python)
- [Library Document](http://fabo.io/doxygen/FaBoBarometer-MPL115-Python/)

## Sample Code
I2Cコネクタに接続したBarometer Brickより、気圧、温度、標高212mの気圧を取得し、シリアルモニタに出力します。

```python
# coding: utf-8
import FaBoBarometer_MPL115
import time
import sys

mpl115 = FaBoBarometer_MPL115.MPL115()

try:
    while True:
        d  = mpl115.readData()
        h = mpl115.readHpa(212.0)

        sys.stdout.write("\rhda = %f, temp = %f, hda_aizu = %f" % (d['hpa'],  d['temp'], h))
        sys.stdout.flush()
        
        time.sleep(1)

except KeyboardInterrupt:
    sys.exit()
```


## Parts
- Freescale(NXP) MPL115A2

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/204_barometer
