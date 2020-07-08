# #601 Motor Shield for Arduino

RaspberryPIの奨励電圧は、5 V, 2.5 Aと定義されている。
PowerCore 20100は、最大電圧が4.8A。

|パーツ|電圧|
|:--|:--|
|DRV8830 |1A |
|RaspberryPI3|2.5A|

## DRV8830

* 動作電圧 2.75V-6.8V
* 最大駆動電流: 1A

## RaspberryPI3

* 動作電圧: 5V
* 奨励電流: 2.5A

## FA-130RA-18100

Noload(無負荷電流)
* 動作電圧: 3V
* 動作電流: 0.15A

Stall(停動電流)
* 動作電圧: 3V
* 動作電流: 2.1A

## ギアボックス

タミヤ ダブルギヤボックス （左右独立4速タイプ) 70168

|ギア比|回転数|回転トルク|
|:--|:--|:--|
|12.7:1|1039rpm|94 gf・cm|
|38.2:1|345rpm|278 gf・cm|
|114.7:1|115rpm|809 gf・cm|
|344.2:1|38rpm|2276 gf・com|

## I2Cプログラム
```python
import smbus
import time
import sys

bus = smbus.SMBus(1)

#スピードは1~58(0x3A)の範囲で指定
def forward(speed):
    cmd = 0x01
    sval = cmd | ((speed+5)<<2)
    bus.write_i2c_block_data(0x64,0x00,[sval])

def back(speed):
    cmd = 0x02
    sval = cmd | ((speed+5)<<2)
    bus.write_i2c_block_data(0x64,0x00,[sval])

def stop():
    bus.write_i2c_block_data(0x64,0x00,[0x00])

def brake():
    bus.write_i2c_block_data(0x64,0x00,[0x03])

#スピードを1~58(0x3A)の範囲で取り出す
def getspeed():
    rd = bus.read_word_data(0x64,0x00)
    speed = (rd >> 2)-5
    return speed

if __name__ == '__main__':
    try:
        for i in range(0x01,0x3A,1):
            forward(i)
            time.sleep(0.1)

        for i in range(0x3A,0x00,-1):
            forward(i)
            time.sleep(0.1)

        for i in range(0x00,0x3A,1):
            back(i)
            time.sleep(0.1)

        for i in range(0x3A,0x00,-1):
            back(i)
            time.sleep(0.1)

        stop()
        brake()
        bus.close()
    except KeyboardInterrupt:
        stop()
        bus.close()
        sys.exit(0)
```

<!--```python-->
<!--import smbus-->
<!--import time-->
<!--bus = smbus.SMBus(1)-->
<!--forward_val = 0x02-->
<!--#変速-->
<!--for i in range(0x06,0x40,1):-->
<!--val = forward_val | (i << 2)-->
<!--bus.write_i2c_block_data(0xc8>>1,0x00,[val])-->
<!--if i % 10 == 0:-->
<!--print i-->
<!--time.sleep(.1)-->
<!---->
<!--for i in range(0x3F,0x05,-1):-->
<!--val = forward_val | (i << 2)-->
<!--bus.write_i2c_block_data(0xc8>>1,0x00,[val])-->
<!--if i % 10 == 0:-->
<!--print i-->
<!--time.sleep(.1)-->
<!--#停止-->
<!--bus.write_i2c_block_data(0xc8>>1,0x00,[0x04])-->
<!--bus.write_i2c_block_data(0xc8>>1,0x00,[0x07])-->
<!---->
<!--bus.close()-->
<!--```-->


