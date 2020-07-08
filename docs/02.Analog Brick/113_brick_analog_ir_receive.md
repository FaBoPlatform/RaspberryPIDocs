# #113 IR Receiver Brick

[](../img/100_analog/product/113.jpg)
<!--COLORME-->

## Overview
フォトトランジスタを使った赤外線受信Brickです。

I/Oピンから赤外線受信のON/OFFを取得することができます。

## 接続
GPIOコネクタに接続します。

### Raspberry PI
![](../img/100_analog/connect/113_connect_with_rasppi.jpg)

## Support
|Arduino|RaspberryPI|IchigoJam|
|:--:|:--:|:--:|
|◯|◯|◯|

## Parts Specification
| Document |
|:--|
| [L-51ROPT1D1](http://akizukidenshi.com/catalog/g/gI-04211/) |
| [2SC1815L-Y](http://akizukidenshi.com/catalog/g/gI-06475/) |

## 回路図
![](../img/100_analog/schematic/113_ir_receive.png)

## Sample Code

GPIO5コネクタに赤外線受信Brick、GPIO4コネクタにLED Brickを接続し、赤外線を受信したらLEDを発光させます。

```python
# coding: utf-8
import RPi.GPIO as GPIO

LED_PIN = 4
IR_RECEIVER_PIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(IR_RECEIVER_PIN, GPIO.IN)

try:
    while True:
        if(GPIO.input(IR_RECEIVER_PIN)):
            GPIO.output(LED_PIN, True)
        else:
            GPIO.output(LED_PIN, False)

except KeyboardInterrupt:
    GPIO.cleanup()

```

## Sample Code

GPIO4コネクタにLED、GPIO5コネクタに赤外線受信Brick、GPIO6コネクタに赤外線LEDBrickを接続
赤外線を受信したらLEDを発光しコールバック関数を呼び、回転数を標準出力に出力する。

```python
import RPi.GPIO as GPIO
import time

i = 0
def callBackTest(channel):
    if GPIO.input(IR_RECEIVER_PIN):
        GPIO.output(LED_PIN, True)
        GPIO.output(LED_PIN, False)
        global i
        i += 1
        print i

LED_PIN = 4
IR_RECEIVER_PIN = 5
IR_LED_PIN = 6

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(IR_LED_PIN, GPIO.OUT)
GPIO.setup(IR_RECEIVER_PIN, GPIO.IN)

GPIO.setup(IR_RECEIVER_PIN, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(IR_RECEIVER_PIN, GPIO.RISING, callback=callBackTest, bouncetime=300)

try:
    while(True):
        GPIO.output(IR_LED_PIN, True)
        time.sleep(0.000001)

except KeyboardInterrupt:
    GPIO.output(IR_LED_PIN, False)
    GPIO.cleanup()
```

## 構成Parts
- 赤外線フォトトランジスタ

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/113_ir_receive
