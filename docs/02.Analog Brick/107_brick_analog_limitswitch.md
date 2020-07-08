# #107 LimitSwitch Brick

[](../img/100_analog/product/107.jpg)
<!--COLORME-->

## Overview
リミットスイッチを使ったBrickです。

I/OピンよりスイッチのON/OFFの状態を取得することができます。

機械の自動停止や位置検出の際に使用します。

## 接続

GPIOコネクタのいずれかに接続します。
### Raspberry Pi
![](../img/100_analog/connect/107_connect_with_rasppi.jpg)

### Arduino
![](../img/100_analog/connect/107_limitswitch_connect.jpg)

## 回路図
![](../img/100_analog/schematic/107_limitswitch.png)

## Sample Code

GPIO5コネクタにLimitSwitch Brickを接続し、GPIO4コネクタに接続したLED Brickの点灯/消灯を制御しています。

```python
# coding: utf-8
import RPi.GPIO as GPIO
import time

LEDPIN = 4
LSPIN = 5   #LimitSwitch pin

led_state = 0

GPIO.setwarnings(False)
GPIO.setmode( GPIO.BCM )
GPIO.setup( LEDPIN, GPIO.OUT )
GPIO.setup( LSPIN, GPIO.IN)

try:
	while True:
    	if( GPIO.input( LSPIN ) ):
        	led_state = 1 - led_state
    		GPIO.output( LEDPIN, led_state )
    		print "led_state: %d " % led_state
    		time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(0)
```

## 構成Parts
- リミットスイッチ

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/107_limitswitch
