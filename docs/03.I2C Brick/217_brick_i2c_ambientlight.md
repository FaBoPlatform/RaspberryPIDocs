# #217 Ambient Light I2C Brick

[](../img/200_i2c/product/217.jpg)
<!--COLORME-->

## Overview
照度センサーを使ったBrickです。

I2Cで明るさを取得することができます。

## 接続
I2Cコネクタへ接続します。

###Arduino
![](../img/200_i2c/connect/217_ambientlight_connect.jpg)
### Raspberry Pi
![](../img/200_i2c/connect/217_connect_with_rasppi.jpg)
## ISL29034 Datasheet
| Document |
| -- |
| [ISL29034 Datasheet](http://www.intersil.com/content/dam/Intersil/documents/isl2/isl29034.pdf) |

## Register
| Slave Address |
| -- |
| 0x44 |

## 回路図
![](../img/200_i2c/schematic/217_ambientlight.png)

## Library

- pipからインストール

```
$sudo pip install FaBoAmbientLight_ISL29034
```
- [Library GitHub](https://github.com/FaBoPlatform/FaBoAmbientLight-ISL29034-Python)
- [Library Document](http://fabo.io/doxygen/FaBoAmbientLight-ISL29034-Python/)

## Sample Code

上記のRapberryPI Python Libraryをインストールしてからご使用ください。

```python
# coding: utf-8
import FaBoAmbientLight_ISL29034
import time
import sys

ISL29034 = FaBoAmbientLight_ISL29034.ISL29034()

try:
    while True:

        lux  = ISL29034.read()

        sys.stdout.write("\rLux=%f" % lux)
        sys.stdout.flush()

        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()
```

## 構成Parts
- Intersil ISL29034

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/217_ambientlight
