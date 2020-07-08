# #207 Temperature I2C Brick

[](../img/200_i2c/product/207.jpg)
<!--COLORME-->

## Overview
温度センサを使用したBrickです。
I2Cでデータを取得できます。

計測できる範囲は−55度〜150度です。

## 接続
I2Cコネクタへ接続します。

### Arduino
![](../img/200_i2c/connect/207_temperature_connect.jpg)
### Raspberry Pi
![](../img/200_i2c/connect/207_connect_with_rasppi.jpg)

## ADT7410 Datasheet
| Document |
| -- |
| [ADT7410 Datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/ADT7410.pdf) |

## Register
| Slave Address |
| -- |
| 0x48 |

## 回路図
![](../img/200_i2c/schematic/207_temperature.png)

## Library

- pipからインストール
```
$ sudo pip install FaBoTemperature_ADT7410
```
- [Library GitHub](https://github.com/FaBoPlatform/FaBoTemperature-ADT7410-Python)
- [Library Document](http://fabo.io/doxygen/FaBoTemperature-ADT7410-Python/)

## Sample Code

```python
# coding: utf-8

import FaBoTemperature_ADT7410
import time
import sys

adt7410 = FaBoTemperature_ADT7410.ADT7410()

try:
    while True:
        t = adt7410.read()
        sys.stdout.write("\rTemp=%f" % t)
        sys.stdout.flush()

        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()
```

## 構成Parts
- Analog Devices ADT7410

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/207_temperature
