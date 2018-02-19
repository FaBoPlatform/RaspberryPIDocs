# Raspberry Pi3用 Fabo WiFi Switch パッケージ

コマンドラインによるWiFi AP / WiFi Static IP / WiFi DHCP Client 切り替えツール

実行ファイル:/opt/fabo/bin/wifi_switch

設定ファイル:/opt/fabo/conf/wifi_switch.conf

## fabo-wifiswitch - v1.0.2
  * 変更点
    * 表示のタイプミスを追加

* WiFi AP / WiFi Static IP / WiFi DHCP Client 切り替えツール
  * https://github.com/FaBoPlatform/RaspberryPIDocs/blob/master/packages/fabo-wifiswitch_1.0.2_armhf.deb
  * 必要なパッケージ:
    * apt-get install hostapd dnsmasq
  * インストール：
    * dpkg -i fabo-wifiswitch_1.0.2_armhf.deb
  * WiFi接続先設定:
    * wpa_passphrase 'SSID' 'PASSWORD' >> /etc/wpa_supplicant/wpa_supplicant.conf
  * 実行:
    * /opt/fabo/bin/wifi_switch --mode ap
  * 設定ファイル:
    * /opt/fabo/conf/wifi_switch.conf
  * ヘルプ
    * /opt/fabo/bin/wifi_switch -h

## fabo-wifiswitch - v1.0.1
  * 変更点
    * 多重起動防止を追加

* WiFi AP / WiFi Static IP / WiFi DHCP Client 切り替えツール
  * https://github.com/FaBoPlatform/RaspberryPIDocs/blob/master/packages/fabo-wifiswitch_1.0.1_armhf.deb
  * 必要なパッケージ:
    * apt-get install hostapd dnsmasq
  * インストール：
    * dpkg -i fabo-wifiswitch_1.0.1_armhf.deb
  * WiFi接続先設定:
    * wpa_passphrase 'SSID' 'PASSWORD' >> /etc/wpa_supplicant/wpa_supplicant.conf
  * 実行:
    * /opt/fabo/bin/wifi_switch --mode ap
  * 設定ファイル:
    * /opt/fabo/conf/wifi_switch.conf
  * ヘルプ
    * /opt/fabo/bin/wifi_switch -h

###### 機能説明
WiFi AP/Static IP/DHCPの設定と切り替えが簡単に出来るように用意
[static|dhcp]モードの時は別途WiFiルータに接続するので、WiFi接続先設定の用意と、staticモードなら設定ファイル(/opt/fabo/conf/wifi_switch.conf)のIPアドレスの設定が必要。

--mode オプション
* apモード
SSID: Pi3-APXXXXXX
PASS: raspberry
本体IPアドレス: 172.31.0.1

* staticモード
本体IPアドレス: static_address=192.168.0.65
接続先ルータIPアドレス: static_gateway=192.168.0.1

* dhcpモード
本体IPアドレス: 任意

実行例
wifi_switch --mode ap

その他オプション
wifi_switch -h

###### 設定の優先順位
コマンドラインオプション > /opt/fabo/conf/wifi_switch.conf > スクリプトデフォルト値


###### インストール手順
```
########################################
# dnsmasq hostapd インストール
# hostapd: WiFiアクセスポイント化
# dnsmasq: DHCP/DNSサーバ
########################################
sudo apt-get update
sudo apt-get install hostapd dnsmasq


########################################
# FaBo WiFi Switchインストール
########################################
sudo wget wget https://github.com/FaBoPlatform/RaspberryPIDocs/raw/master/packages/fabo-wifiswitch_1.0.2_armhf.deb
sudo dpkg -i fabo-wifiswitch_1.0.2_armhf.deb

# /root/.bashrcに追記
sudo sh -c "echo 'export PATH=\$PATH:/opt/fabo/bin' >> /root/.bashrc"


########################################
# IPv4 Forwarding
########################################
sudo vi /etc/sysctl.conf
net.ipv4.ip_forward=1

# IP転送を有効にする
sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"

# IP転送が有効になっているかどうか確認する
/sbin/sysctl net.ipv4.ip_forward


########################################
# dhcpcdがwlan0を使わないようにする
########################################
sudo sh -c "echo 'denyinterfaces wlan0' >> /etc/dhcpcd.conf"


########################################
# WiFi接続先設定
########################################
sudo sh -c "wpa_passphrase 'SSID' 'PASSWORD' >> /etc/wpa_supplicant/wpa_supplicant.conf"

sudo vi /etc/wpa_supplicant/wpa_supplicant.conf
country=JP


########################################
# WiFi モード切替
########################################
sudo /opt/fabo/bin/wifi_switch --mode ap


########################################
# アンインストール
########################################
apt-get remove fabo-wifiswitch


```