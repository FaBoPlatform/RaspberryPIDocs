# #102 Buzzer Brick

RaspberryPIはRev 1.0.9から対応しています。

![](../img/100_analog/product/102_v10.jpeg)
<!--COLORME-->

※写真は、Rev 1.0.10のものです。

## Overview
圧電ブザーを使ったBrickです。I/Oピンより、鳴らす音や音の長さを制御することができます。

## 接続
### RaspberyPi
GPIO12 に接続します。

![](../img/100_analog/connect/102_buzzer_connect.jpeg)

※写真は、ラズパイモーターシールドとの接続の場合です。

## Support
|Arduino|RaspberryPi|IchigoJam|
|:--:|:--:|:--:|
|◯|◯|◯|

## 回路図

![](../img/100_analog/schematic/102_buzzer_v10.png)

## Sample Code

PWMを発生させて圧電ブザーを鳴らします。どのGPIOでも鳴らすことができますが、ソフトウェアPWMとなり波形が完全に近い周期にはなりません。
そのため遅延がないハードウェアPWMを使用します。ハードウェアGPIOにはあらかじめピンが決まっており今回はGPIO12を使用します。
ライブラリはpigpioを使用します。最近のラズベリアンにはデフォルトでインストールされています。（2019.2.1現在）


GPIOピン設定確認

FaBoのシールドのピンGPIO12（ピンはラズパイ３２、チップであるBCMピン １２）になります。

$gpio readall

pigpiodデーモン実行

$sudo pigpiod

viエディタなどを使って下記のコード編集します。

$sudo vi hardwarepwm.py

```python

#!/usr/bin/env python
# coding: utf-8

import pigpio
import time

pig = pigpio.pi()
pig.set_mode(12, pigpio.ALT0)

counter = 0
while (counter < 3):
    pig.hardware_PWM(12, 261, 400)
    time.sleep(1)
    pig.hardware_PWM(12, 293 ,400)
    time.sleep(1)
    pig.hardware_PWM(12, 329, 400)
    time.sleep(1)
    counter = counter + 1
    pig.hardware_PWM(12, 50, 0)
    time.sleep(1)

pig.hardware_PWM(12, 50, 0)
pig.stop()

```

スーパーユーザーなしで実行可能にします。

$sudo chmod 755 hardwarepwm.py

ドレミソースコード実行

$python hardwarepwm.py

## Parts
- 圧電ブザー

TDK PS1740P02E データシート
https://product.tdk.com/info/ja/catalog/datasheets/piezoelectronic_buzzer_ps_ja.pdf

## GitHub

- https://github.com/FaBoPlatform/FaBo/tree/master/102_buzzer

##  参考

GPIO functions
https://elinux.org/RPi_BCM2835_GPIOs

