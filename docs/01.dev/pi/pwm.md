# RaspberryPIのPWM対応表

|PIN|PI Zero|PI3|
|:--|:--:|:--:|
|GPIO4|○|○|
|GPIO5|○|○|
|GPIO6|○|○|
|GPIO12|○|○|
|GPIO13|○|○|
|GPIO16|○|○|
|GPIO17|○|○|
|GPIO18|○|○|
|GPIO19|○|○|
|GPIO20|○|○|
|GPIO21|○|○|
|GPIO22|○|○|
|GPIO24|○|○|
|GPIO25|○|○|
|GPIO26|○|○|

全てのピンでソフトウェアPWMを出力できます。

## 検証コード

LEDの輝度の変化を目視確認。

```python
# coding: utf-8
import RPi.GPIO as GPIO
import time

PWM_PIN = 4

GPIO.setwarnings(False)
GPIO.setmode( GPIO.BCM )
GPIO.setup(PWM_PIN, GPIO.OUT )

LED = GPIO.PWM(PWM_PIN, 100)
LED.start(0)

if __name__ == '__main__':
value = 0
try:
while True:
LED.ChangeDutyCycle(value % 100)
time.sleep(0.01)
value += 1
except KeyboardInterrupt:
LED.stop()
GPIO.cleanup()
sys.exit(0)
```

必ず最後に
```python
LED.stop()
```
を入れてください。次にRPi.GPIOを使ってPWMを出力する時に不安定になります。
