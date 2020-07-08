# Display

[RASPBERRY PI TOUCH DISPLAY](https://www.raspberrypi.org/products/raspberry-pi-touch-display/)の装着方法に関して解説しています。

## Display側の装着

![](../img/dev/pi/display001.png)


## RaspberryPI側の装着

![](../img/dev/pi/display002.png)


## 画面の回転、反転

`/boot/config.txt`
```
#最後に追記
#180度回転
lcd_rotate = 2

#横方向に反転する
lcd_rotate = 0x10000

#縦方向に反転する
lcd_rotate = 0x20000
```
