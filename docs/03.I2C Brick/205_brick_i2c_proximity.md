# #205 Proximity I2C Brick

[](../img/200_i2c/product/205.jpg)
<!--COLORME-->

## Overview
近接センサーを使ったBrickです。

I2Cでデータを取得できます。

## 接続
I2Cコネクタへ接続します。

### Arduino
![](../img/200_i2c/connect/205_proximity_connect.jpg)
### Raspberry Pi
![](../img/200_i2c/connect/205_connect_with_rasppi.jpg)

## VCNL4010 Datasheet
| Document |
|:--|
| [VCNL4010 Datasheet](https://www.adafruit.com/images/product-files/466/vcnl4010.pdf) |

## Register
| I2C Slave Address |
|:-- |
| 0x13 |

## 回路図
![](../img/200_i2c/schematic/205_proximity.png)

## Library

- pipからインストール

```shell
$ sudo pip install FaBoProximity_VCNL4010
```
- [Library GitHub](https://github.com/FaBoPlatform/FaBoProximity-VCNL4010-Python)
- [Library Document](http://fabo.io/doxygen/FaBoProximity-VCNL4010-Python/)

## Sample Code

上記のRapberryPI Python Libraryをインストールしてからご使用ください。

```python
# coding: utf-8
import FaBoProximity_VCNL4010
import time
import sys

vcnl4010 = FaBoProximity_VCNL4010.VCNL4010()

try:
    while True:
        p = vcnl4010.readProx()
        a = vcnl4010.readAmbi()
        sys.stdout.write("\rProx=%f, Ambi=%f" % (p,  a))
        sys.stdout.flush()

        time.sleep(1)

except KeyboardInterrupt:
    sys.exit()
```

## Parts
- Vishay VCNL4010

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/205_proximity
