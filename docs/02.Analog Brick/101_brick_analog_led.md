# #101 LED Brick

[](../img/100_analog/product/101.jpg)
<!--COLORME-->

## Overview
LEDのBrickです。発光色は5色（青・緑・赤・白・黄）あります。Lチカのおともにもどうぞ。

※購入時は色の間違いにご注意ください。

## 接続

GPIOコネクタのいずれかに接続します。
### Raspberry Pi
![](../img/100_analog/connect/101_connect_with_rasppi.jpg)

### Arudio
![](../img/100_analog/connect/101_led_connect.jpg)


## 回路図
![](../img/100_analog/schematic/101_led.png)

## Sample Code

GPIO4コネクタにLED Brickを接続し、一定時間ごとに点灯/消灯させています。

```python
# coding: utf-8
import RPi.GPIO as GPIO
import time
import sys

LEDPIN = 4

GPIO.setwarnings(False)
GPIO.setmode( GPIO.BCM )
GPIO.setup( LEDPIN, GPIO.OUT )

try:
	while True:
		GPIO.output( LEDPIN, True )
		time.sleep( 1.0 )
		GPIO.output( LEDPIN, False )
		time.sleep( 1.0 ) 
except KeyboardInterrupt:
	GPIO.cleanup()
	sys.exit(0)
```

PWMによる転送をおこないます。

```python
# coding: utf-8
import RPi.GPIO as GPIO
import time
import sys

LEDPIN = 4

GPIO.setwarnings(False)
GPIO.setmode( GPIO.BCM )
GPIO.setup( LEDPIN, GPIO.OUT )
LED = GPIO.PWM(LEDPIN, 100)
value = 0

try:
	while True:
	LED.ChangeDutyCycle(value % 100)
	time.sleep(0.01)
	value += 1
except KeyboardInterrupt:
	GPIO.cleanup()
	sys.exit(0)
```

## 構成Parts
- 5mm LED(各色)

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/101_led
