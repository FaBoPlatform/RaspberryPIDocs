# #103 Button Brick

[](../img/100_analog/product/103.jpg)
<!--COLORME-->

## Overview
ボタンを使ったBrickです。I/OピンよりボタンのON/OFFの状態を取得することができます。

※ボタンカバー部分の色はランダムで送付するため色のご指定はできません。あらかじめご了承ください。

## 接続

GPIOコネクタのいずれかに接続します。

### Raspberr Pi
![](../img/100_analog/connect/103_connect_with_rasppi.jpg)


### Arduino
![](../img/100_analog/connect/103_button_connect.jpg)

## 回路図
![](../img/100_analog/schematic/103_button.png)

## Sample Code

GPIO5コネクタに接続したButton Brickの入力により、GPIO4コネクタに接続したLED Brick の点灯/消灯を制御しています。

```python
# coding: utf-8
import RPi.GPIO as GPIO
import sys

LEDPIN = 4
BUTTONPIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN, GPIO.OUT)
GPIO.setup(BUTTONPIN, GPIO.IN)

try:
	while True:
		# ボタン押下判定
		if( GPIO.input(BUTTONPIN)):
			# LED点灯
			GPIO.output(LEDPIN, True)
		else:
			# LED消灯
			GPIO.output(LEDPIN, False)
except KeyboardInterrupt:
	GPIO.cleanup()
	sys.exit(0)
```


## 構成Parts
- 12mm角タクトスイッチ

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/103_button
