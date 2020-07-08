# #203 Color I2C Brick

[](../img/200_i2c/product/203.jpg)
<!--COLORME-->

## Overview
カラーセンサを使用したBrickです。

センサーより読み取った赤、緑、青、赤外線(明るさ)の4つのデータを、I2Cにて取得することができます。

## 接続
I2Cコネクタへ接続します。

### Arduino
![](../img/200_i2c/connect/203_color_connect.jpg)

### Raspberry Pi
![](../img/200_i2c/connect/203_connect_with_rasppi.jpg)

## S11059 Datasheet
| Document |
| -- |
| [S11059 Datasheet](http://www.hamamatsu.com/resources/pdf/ssd/s11059-02dt_etc_kpic1082j.pdf) |

## Register
| Slave Address |
| -- |
| 0x2A |

## 回路図
![](../img/200_i2c/schematic/203_color.png)

## Library

- pipからインストール
```
pip install FaBoColor_S11059
```
- [Library GitHub](https://github.com/FaBoPlatform/FaBoColor-S11059-Python)
- [Library Document](http://fabo.io/doxygen/FaBoColor-S11059-Python/)

## Sample Code

```python
# coding: utf-8
import FaBoColor_S11059
import time
import sys

s11059 = FaBoColor_S11059.S11059()

try:
    while True:
        c = s11059.read()
        sys.stdout.write("\rr=%f, g=%f, b=%f, ir=%f" % (c['r'],  c['g'], c['b'], c['ir']))
        sys.stdout.flush()
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit()
```

## Parts
- HAMAMATSU S11059

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/203_color
