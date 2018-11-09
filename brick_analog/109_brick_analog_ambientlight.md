# #109 Light Brick

<center>![](/img/100_analog/product/109.jpg)
<!--COLORME-->

## Overview
CDSセルを使用した光センサーBrickです。

周囲の明るさの変化をアナログ値として取得することができます。

## Connecting

アナログコネクタ(A0〜A7)のいずれかに接続します。
### Arduino
![](/img/100_analog/connect/109_ambientlight_connect.jpg)

### Raspberr Pi
![](/img/100_analog/connect/109_connect_with_rasppi.jpg)


### IchigoJam
アナログ用コネクタ(IN2またはANA()で設定したコネクタ)のどれかに接続します。


## Parts Specification
| Document |
|:--|
| [MI527](http://akizukidenshi.com/catalog/g/gI-00110/) |

## Schematic
![](/img/100_analog/schematic/109_light.png)

## Sample Code

A0コネクタにLight Brickを接続して、GPIO4コネクタに接続したLED Brickの明るさ調節に使用しています。

```python
# coding: utf-8
import RPi.GPIO as GPIO
import spidev
import time
import sys

# A0コネクタにLightを接続
LIGHTPIN = 0

# GPIO4コネクタにLEDを接続
LEDPIN = 4

# GPIOポートを設定
GPIO.setwarnings(False)
GPIO.setmode( GPIO.BCM )
GPIO.setup( LEDPIN, GPIO.OUT )

def readadc(channel):
	adc = spi.xfer2([1,(8+channel)<<4,0])
	data = ((adc[1]&3) << 8) + adc[2]
	return data

def arduino_map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# PWM/100Hzに設定
LED = GPIO.PWM(LEDPIN, 100)

# 初期化
LED.start(0)
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 5000

try:
	while True:
		ambient = readadc(LIGHTPIN)
		sys.stdout.write("\rambient = %f" % (ambient))
        sys.stdout.flush()
		value = arduino_map(ambient, 0, 1023, 0, 100)
		LED.ChangeDutyCycle(value)
		time.sleep( 0.01 )
except KeyboardInterrupt:
	LED.stop()
	GPIO.cleanup()
	spi.close()
	sys.exit(0)
```

## 構成Parts
- CDSセル(5mm)

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/109_light
