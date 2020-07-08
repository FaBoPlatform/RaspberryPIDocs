# I2C Kernel/smbus修正
Raspbian Stretch Liteはraspi-configでI2Cを有効にしてもsmbusコード実行時にエラーが発生します。原因はKernelにあるようなので修正します。<br>

```
wget -O i2c1-bcm2708.dtbo https://drive.google.com/uc\?export=download\&id=0B_P-i4u-SLBXb3VlN0N5amVBb1k
sudo chmod 755 i2c1-bcm2708.dtbo
sudo chown root:root i2c1-bcm2708.dtbo
sudo mv i2c1-bcm2708.dtbo /boot/overlays/
sudo echo "dtoverlay=i2c1-bcm2708" >> /boot/config.txt
sudo reboot
# リブート後、Raspberry Pi3に再ログインしてから継続
sudo sh -c '/bin/echo Y > /sys/module/i2c_bcm2708/parameters/combined'
sudo reboot
```

参考： <br>
* [https://github.com/raspberrypi/firmware/issues/867](https://github.com/raspberrypi/firmware/issues/867)
* [https://www.raspberrypi.org/forums/viewtopic.php?t=192958](https://www.raspberrypi.org/forums/viewtopic.php?t=192958)
* [https://github.com/raspberrypi/firmware/issues/828](https://github.com/raspberrypi/firmware/issues/828)
