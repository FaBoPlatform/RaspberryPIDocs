# #212 LCD I2C Brick

[](../img/200_i2c/product/212.jpg)
<!--COLORME-->

## Overview
LCDを使用したBrickです。

I2Cで表示データを制御できます。

## 接続
I2Cコネクタへ接続します。

### Arduino
![](../img/200_i2c/connect/212_lcd_connect.jpg)
### Raspberry Pi
![](../img/200_i2c/connect/212_connect_with_rasppi.jpg)

## PCF8574 Datasheet
| Document |
|:--|
| [PCF8574 Datasheet](http://www.tij.co.jp/jp/lit/ds/symlink/pcf8574.pdf) |

## Register
| A0 | A1 | A2 | Slave Address |
| -- | -- | -- | -- |
| LOW | LOW | LOW | 0x20 |

FaBo Brickでは、初期値に0x20が設定されています。Brick表面のソルダージャンパーで設定を変更できます。

## 回路図
![](../img/200_i2c/schematic/212_lcd.png)

## Library

- pipからインストール
```
pip install FaBoLCD_PCF8574
```
- [Library GitHub](https://github.com/FaBoPlatform/FaBoLCD-PCF8574-Python)
- [Library Document](http://fabo.io/doxygen/FaBoLCD-PCF8574-Python/)

## Sample Code

上記のRapberryPI Python Libraryをインストールしてからご使用ください。

```python
# coding: utf-8
## @package FaBoLCD_PCF8574
#  This is a library for the FaBo LCD I2C Brick.
#
#  http://fabo.io/212.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import FaBoLCD_PCF8574
import time
import sys

i = 0
lcd = FaBoLCD_PCF8574.PCF8574()

lcd.write("Hello, World!")

try:
    while True:
        lcd.setCursor(0,1)
        lcd.write(i)

        i += 1

        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()
```

## 構成Parts
- PCF8574
- LCD 1602A

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/212_lcd
