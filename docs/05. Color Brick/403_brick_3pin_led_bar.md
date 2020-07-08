# #403 ColorLED Bar

[](../img/400_led/product/403.jpg)
<!--COLORME-->

## Overview
RGB Color LEDをBar状に5個配置したBrickです。

## 接続
アナログコネクタ(A0〜A5)、またはデジタルコネクタ(2〜13)のどれかに接続します。

### Arduino
![](../img/400_led/connect/403_ledbar_connect.jpg)
### Raspberry Pi
![](../img/400_led/connect/403_connect_with_rasppi.jpg)

## Support
|Arduino|RaspberryPI|
|:--:|:--:|
|◯|◯|

## WS2812B Datasheet
|Document|
|--|
|[WS2812B Datasheet](http://www.adafruit.com/datasheets/WS2812B.pdf)|

## 回路図
![](../img/400_led/schematic/403_led_bar.png)

## Libraryの設定

```
$ sudo apt-get install scons swig
$ git clone https://github.com/jgarff/rpi_ws281x.git
$ cd rpi_ws281x
$ scons
$ cd python
$ sudo python setup.py install
```

## Sample

```python
# coding: utf-8
import time
from neopixel import *

# LED strip configuration:
LED_COUNT = 5  # LEDの数.
LED_PIN = 18      # Color LED Brickの接続先.
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5 # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 100 # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# Color sensor
c = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
c.begin()

m = 0
while True:
    c.setPixelColor(0, Color(m,0,0)) 
    c.setPixelColor(1, Color(0,m,0)) 
    c.setPixelColor(2, Color(0,0,m)) 
    c.setPixelColor(3, Color(m,0,m)) 
    c.setPixelColor(4, Color(m,m,0)) 
    c.show()
    m += 1
    if m > 255:
      m = 0
    time.sleep(0.01)
```

## Parts
- RGB LED WS2812B

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/403_led_bar
