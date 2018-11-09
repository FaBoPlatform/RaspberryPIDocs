# #108 Temperature Brick
<center>![](/img/100_analog/product/108.jpg)
<!--COLORME-->

## Overview
温度を計測するBrickです。

アナログ値(0〜1023)を取得でき、変換することで−30度から100度までの温度を計測することができます。

## Connecting

アナログコネクタ(A0〜A7)のいずれかに接続します。
### Arduino
![](/img/100_analog/connect/108_temperature_connect.jpg)

### Raspberr Pi
![](/img/100_analog/connect/104_connect_with_rasppi.jpg)

## LM61CIZ Datasheet
| Document |
|:--|
| [LM61CIZ Datasheet](http://akizukidenshi.com/catalog/g/gI-02726/) |

## Schematic
![](/img/100_analog/schematic/108_temperature.png)


## Sample Code

A0コネクタに接続したTemperature Brickにより温度を計測します。

```python
# coding: utf-8
import spidev
import time
import sys

# A0コネクタにTemperatureを接続
TEMPPIN = 0

def readadc(channel):
	adc = spi.xfer2([1,(8+channel)<<4,0])
	data = ((adc[1]&3) << 8) + adc[2]
	return data

def arduino_map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# 初期化
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 5000

try:
	while True:
		data = readadc(TEMPPIN)
		volt = arduino_map(data, 0, 1023, 0, 5000)
		temp = arduino_map(volt, 300, 1600, -30, 100)
		sys.stdout.write("\rtemp = %f" % (temp))
        sys.stdout.flush()
		time.sleep( 0.5 )
except KeyboardInterrupt:
	spi.close()
	sys.exit(0)
```

## 構成Parts
- IC温度センサ LM61CIZ

## GitHub
- https://github.com/FaBoPlatform/FaBo/tree/master/108_temperature
