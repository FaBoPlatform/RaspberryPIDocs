# Servo

#### サーボを動かすサンプルコード

```python
# coding: utf-8
import RPi.GPIO as GPIO
import time

SERVOPIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVOPIN,GPIO.OUT)
servo=GPIO.PWM(SERVOPIN,50)
servo.start(0.0)
for i in range(2,11):
       servo.ChangeDutyCycle(i)
       time.sleep(1)
servo.stop()
```

`GPIO.setup(23,GPIO.OUT)`はGPIO23ピンを出力ピンとする  
`servo=GPIO.PWM(23,50)`はPWM波が１つの波形が２０msなので５０Hz指定  
`servo.ChangeDutyCycle(i)`ここで引数はfloatでもいける  
`servo.stop()`を必ず最後に入れる。次にPWMを使おうとすると正常にPWM波が出なくなる。
