# #112 IR LED Brick

[](../img/100_analog/product/112.jpg)
<!--COLORME-->

## Overview
赤外線LEDを使ったBrickです。

I/Oピンから赤外線LEDをON/OFFを制御することができます。

## 接続

OUTコネクタのいずれかに接続します。

### Raspberry Pi
![](../img/100_analog/connect/112_connect_with_rasppi.jpg)

## Parts Specification
| Document |
|:--|
| [OSI5LA5113A](http://akizukidenshi.com/catalog/g/gI-04311/) |

## 回路図
![](../img/100_analog/schematic/112_ir_led.png)

## Sample Code

A0コネクタに赤外線LED Brickを接続し、１秒間隔で赤外線LEDを発光させます。

```python
# coding: utf-8
import RPi.GPIO as GPIO
import time
import sys

IR_LED_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(IR_LED_PIN, True)
        time.sleep(1.0)
        GPIO.output(IR_LED_PIN, False)
        time.sleep(1.0)

except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()

```

## 構成Parts
- 5mm 赤外線LED OSI5LA5113A

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/112_ir_led
