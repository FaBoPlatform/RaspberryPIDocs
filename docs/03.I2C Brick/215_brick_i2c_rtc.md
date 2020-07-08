# #215 RTC I2C Brick

[](../img/200_i2c/product/215.jpg)
<!--COLORME-->

## Overview
リアルタイムクロックを使用したBrickです。
I2Cでデータを取得できます。

## 接続
I2Cコネクタへ接続します。

###Arduino
![](../img/200_i2c/connect/215_rtc_connect.jpg)
### Raspberry Pi
![](../img/200_i2c/connect/215_connect_with_rasppi.jpg)

## PCF2129 Datasheet
| Document |
| -- |
| [PCF2129 Datasheet](http://cache.nxp.com/documents/data_sheet/PCF2129.pdf) |

## Register
| Slave Address |
| -- |
| 0x51 |

## 回路図
![](../img/200_i2c/schematic/215_rtc.png)

- pipからインストール
```
pip install FaBoRTC_PCF2129
```
- [Library GitHub](https://github.com/FaBoPlatform/FaBoRTC-PCF2129-Python)
- [Library Document](http://fabo.io/doxygen/FaBoRTC-PCF2129-Python/)

## Sample Code

上記のRapberryPI Python Libraryをインストールしてからご使用ください。

```python
# coding: utf-8
## @package FaBoRTC_PCF2129
#  This is a library for the FaBo RTC I2C Brick.
#
#  http://fabo.io/215.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import FaBoRTC_PCF2129
import time
import sys

rtc = FaBoRTC_PCF2129.PCF2129()


try:
    # 日付時刻の設定
    print "set date/time"
    rtc.setDate(
        2016, # Years
        7,    # months
        8,    # days
        12,   # hours
        1,    # minutes
        50)   # seconds

    while True:
        # 日付時刻の取得
        now = rtc.now()

        # 日付時刻の表示
        sys.stdout.write(str(now['year'])  + '/')
        sys.stdout.write(str(now['month']).zfill(2) + '/')
        sys.stdout.write(str(now['day']).zfill(2)   + ' ')

        sys.stdout.write(str(now['hour']).zfill(2)    + ':')
        sys.stdout.write(str(now['minute']).zfill(2)  + ':')
        sys.stdout.write(str(now['second']).zfill(2))
        print
        time.sleep(1)

except KeyboardInterrupt:
    sys.exit()
```


## 構成Parts
- NXP PCF2129

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/215_rtc
