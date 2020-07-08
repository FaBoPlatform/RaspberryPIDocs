# #116 Distance Brick

[](../img/100_analog/product/116.jpg)
<!--COLORME-->

## Overview
距離センサーモジュールを使用したBrickです。

I/Oピンより距離センサーの正面についているレンズから物体までの距離をアナログ値(0〜1023)で取得することができます。

測定可能な距離は10〜80cmとなっています。

## 接続

アナログコネクタ(A0〜A7)のいずれかに接続します。
### Raspberr Pi
![](../img/100_analog/connect/116_connect_with_rasppi.jpg)


## GP2Y0A21YK Datasheet
| Document |
| -- |
| [GP2Y0A21YK Datasheet](http://www.sharpsma.com/webfm_send/1208) |

## Sample Code

A0コネクタに接続し、距離を計測します。

```python
# coding: utf-8
import spidev
import time
import sys

# A0コネクタにDistanceを接続
DISTANCE_PIN = 0

def readadc(channel):
    adc = spi.xfer2([1, (8+channel)<<4, 0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

def arduino_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# 初期化
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 5000

try:
    while True:
        data = readadc(DISTANCE_PIN)
        # 取得した値を電圧(mv)に変換
        volt = arduino_map(data, 0, 1023, 0, 5000)
        # 電圧から距離(cm)に変換
        distance = arduino_map(volt, 3200, 500, 5, 80)
        print("distance : {:3} ".format(distance))
        time.sleep(0.05)
except KeyboardInterrupt:
    spi.close()
    sys.exit(0)
```

## 構成Parts
- 距離センサーモジュール GP2Y0A21YK

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/116_distance
