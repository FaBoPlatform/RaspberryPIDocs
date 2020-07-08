# Raspberry Pi3用 Fabo WiFi Switch GPIO Daemon パッケージ

Fabo基板付属のWiFi切り替えスイッチによる WiFi AP / WiFi DHCP Client 切り替えツール


## fabo-wifiswitch-gpiod - v1.0.1
  * 変更点
    * ジャンパピン[N-REST]が接続されていない時に、デフォルト設定に戻すように変更

* Fabo WiFi Switch GPIO Daemon: Fabo基板付属のWiFi切り替えスイッチによる WiFi AP / WiFi DHCP Client 切り替えツール
  * https://github.com/FaBoPlatform/RaspberryPIDocs/blob/master/packages/fabo-wifiswitch-gpiod_1.0.1_armhf.deb
  * 必要なパッケージ:
    * [fabo-wifiswitch v1.0.1](./fabo-wifiswitch.md) 以上
    * apt-get install python-pip python-rpi.gpio
    * pip install futures
  * インストール：
    * dpkg -i fabo-wifiswitch-gpiod_1.0.1_armhf.deb


###### 機能説明
ジャンパピン[N-REST]が接続されていない時、以下のコマンドが実行され設定ファイルが初期化される。
  * /opt/fabo/bin/wifi_switch --print-config > /opt/fabo/conf/wifi_switch.conf

confファイルを変更している場合は設定ファイルを初期化しないようにジャンパピンを接続しておくこと。

MODEスイッチが[AP]の時、以下のコマンドが実行され、APモードに切り替わる。（Raspberry Piがルータになる）
  * /opt/fabo/bin/wifi_switch --mode ap

SSID: RP3-APXXXXXX
PASSWORD: raspberrypi

MODEスイッチが[Slave]の時、以下のコマンドが実行され、DHCPモードに切り替わる。（ルータに接続する）
  * /opt/fabo/bin/wifi_switch --mode dhcp


###### インストール手順
```
########################################
# FaBo WiFi Switch GPIO Daemonインストール
########################################
sudo apt-get install python-pip python-rpi.gpio
sudo pip install futures
sudo wget https://raw.githubusercontent.com/FaBoPlatform/RaspberryPIDocs/master/packages/fabo-wifiswitch-gpiod_1.0.1_armhf.deb
sudo dpkg -i fabo-wifiswitch-gpiod_1.0.1_armhf.deb
sudo systemctl enable wifi_switchd
sudo systemctl start wifi_switchd


########################################
# アンインストール
########################################
apt-get remove fabo-wifiswitch-gpiod


```