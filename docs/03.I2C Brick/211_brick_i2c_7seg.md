# #211 7Segment LED I2C Brick

[](../img/200_i2c/product/211.jpg)
<!--COLORME-->

## Overview
７セグメントLEDを使ったBrickです。

I2Cで表示パターンを制御できます。

## 接続
I2Cコネクタへ接続します。

### Arduino
[](../img/200_i2c/connect/211_7seg_connect.jpg)
### Raspberry Pi
![](../img/200_i2c/connect/211_connect_with_rasppi.jpg)
## TLC59208F Datasheet
| Document |
| -- |
| [TLC59208F Datasheet](http://www.ti.com/jp/lit/gpn/tlc59208f) |

## Register
| A0 | A1 | A2 | Slave Address |
| -- | -- | -- | -- |
| LOW | LOW | LOW | 0x20 |

FaBo Brickでは、初期値に0x20が設定されています。Brick裏面のソルダージャンパーで設定を変更できます。

## 回路図
![](../img/200_i2c/schematic/211_7seg.png)

## Library

- pipからインストール
```
sudo pip install FaBo7Seg_TLC59208
```
- [Library GitHub](https://github.com/FaBoPlatform/FaBo7Segment-TLC59208-Python)
- [Library Document](http://fabo.io/doxygen/FaBo7Segment-TLC59208-Python/)

## Sample Code
PWM出力値は、"0x02"でほぼ視認できる明るさで点灯されます。あまり高い数値にすると、点灯しなくなるおそれがあります。

### Sample Code1

I2Cコネクタに7seg Brickを接続し、「0〜９」を順番に表示させます。

```python
# coding: utf-8
import FaBo7Seg_TLC59208
import time

tlc59208 = FaBo7Seg_TLC59208.TLC59208()

try:
    while True:
        for i in xrange(10):
            tlc59208.showNumber(i)
            time.sleep(0.5)

except KeyboardInterrupt:
    tlc59208.showNumber(10)
```

### Sample Code2

それぞれの部位を光らせます。

```python
# coding: utf-8
import FaBo7Seg_TLC59208
import time

tlc59208 = FaBo7Seg_TLC59208.TLC59208()

try:
    while True:
        tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PIN_A | FaBo7Seg_TLC59208.LED_PIN_G | FaBo7Seg_TLC59208.LED_PIN_D);
        time.sleep(1)
        for i in xrange(10):
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM5)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM4)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM2)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM1)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM0)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM6)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM5)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM4)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM2)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM1)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM0)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM6)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_PWM5)
            time.sleep(0.05)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_OFF)
            time.sleep(0.05)

            tlc59208.showNumber(i)
            time.sleep(1)
            tlc59208.showDot()
            time.sleep(1)
            tlc59208.showPattern(FaBo7Seg_TLC59208.LED_OFF)
            time.sleep(1)
except KeyboardInterrupt:
    tlc59208.showPattern(FaBo7Seg_TLC59208.LED_OFF)
```


## 構成Parts
- 7セグメントLED
- Texas Instruments TLC59208F

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/211_7seg
