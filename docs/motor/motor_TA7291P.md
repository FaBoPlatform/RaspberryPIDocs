# #モータードライバーTA7291Pのサンプルコード


## プログラム
```python
# coding: utf-8
import RPi.GPIO as GPIO
import time

MOTORPIN1 = 4
MOTORPIN2 = 5
MOTOR_LEVEL_PIN = 18
POWER_PIN = 17

GPIO.setwarnings(False)
GPIO.setmode( GPIO.BCM )
GPIO.setup(MOTOR_LEVEL_PIN, GPIO.OUT )
GPIO.setup(MOTORPIN1, GPIO.OUT )
GPIO.setup(MOTORPIN2, GPIO.OUT )

#基準用の3.3Vを確保するために使用
GPIO.setup(POWER_PIN, GPIO.OUT )
GPIO.output( POWER_PIN, True )

# PWM/100Hzに設定
MOTOR_LEVEL = GPIO.PWM(MOTOR_LEVEL_PIN, 100)
# 初期化
MOTOR_LEVEL.start(0)

if __name__ == '__main__':
    try:
        #モーター正転
        GPIO.output( MOTORPIN1, True )
        GPIO.output( MOTORPIN2, False )
        #速度変更
        for i in range(10,101,10):
            MOTOR_LEVEL.ChangeDutyCycle(i)
            time.sleep(1)
        #モーターストップ
        GPIO.output( MOTORPIN1, False )
        GPIO.output( MOTORPIN2, False )
        MOTOR_LEVEL.stop()
        GPIO.cleanup()
    except KeyboardInterrupt:
        MOTOR_LEVEL.stop()
        GPIO.cleanup()
        sys.exit(0)
```
