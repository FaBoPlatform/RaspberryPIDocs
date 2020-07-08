# #208 Humidity I2C Brick

[](../img/200_i2c/product/208.jpg)
<!--COLORME-->

## Overview
湿度センサを使用したBrickです。
I2Cでデータを取得できます。

## 接続
I2Cコネクタへ接続します。

### Arduino
![](../img/200_i2c/connect/208_humidity_connect.jpg)
### Raspberry Pi
![](../img/200_i2c/connect/208_connect_with_rasppi.jpg)
## HTS221 Datasheet
| Document |
| -- |
| [HTS221 Datasheet](http://www2.st.com/content/ccc/resource/technical/document/datasheet/4d/9a/9c/ad/25/07/42/34/DM00116291.pdf/files/DM00116291.pdf/jcr:content/translations/en.DM00116291.pdf) |

## Register
| Slave Address |
| -- |
| 0x5F |

## 回路図
![](../img/200_i2c/schematic/208_humidity_hts221.png)

## Library

- pipからインストール

```
$ sudo pip install FaBoHumidity_HTS221
```

- [Library GitHub](https://github.com/FaBoPlatform/FaBoHumidity-HTS221-Python)
- [Library Document](http://fabo.io/doxygen/FaBoHumidity-HTS221-Python/)

## Sample Code

上記のRapberryPI Python Libraryをインストールしてからご使用ください。
```python
# coding: utf-8
import FaBoHumidity_HTS221
import time
import sys

hts221 = FaBoHumidity_HTS221.HTS221()

try:
    while True:
        h = hts221.readHumi()
        t = hts221.readTemp()
        sys.stdout.write("\rHumidity=%f,Temp=%f" % (h, t))
        sys.stdout.flush()
        time.sleep(1)

except KeyboardInterrupt:
    sys.exit()
```

## 構成Parts
- STMicroelectronics HTS221

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/208_humidity
