
stapdとWifiClientの切り替え(SwitchBrick(#117)使用)

前項: 「hostapdとWifiClientの切り替え」が行ってあることが前提です。

切り替えを[SwitchBrick(#117)](http://docs.fabo.io/fabo/rasppi/brick_analog/117_brick_analog_slideswitch.html)で行うことが出来るように、各種変更します。

- - -

### 切り替えの検出用スクリプト

`~/.ap/toggle_sw.py`として、切り替えをしたか判定するスクリプトを書いて配置します。

~/.ap/toggle_sw.py
``` python 
import RPi.GPIO as GPIO
import time
import os

LEDPIN = 4
SWPIN = 5   #LimitSwitch pin


GPIO.setwarnings(False)
GPIO.setmode( GPIO.BCM )
GPIO.setup( LEDPIN, GPIO.OUT )
GPIO.setup( SWPIN, GPIO.IN)

if(GPIO.input(SWPIN) ):
    os.system("echo 1 > /home/pi/.ap_mode")
else:
    os.system("echo 0 > /home/pi/.ap_mode")
```

これにより、`~/.ap_mode`をスイッチのON,OFFで書き換えれるようにします。

- - -

### 起動時に自動実行

これを`/etc/rc.local`に以下のように記述します

``` bash
...

set -- $_IP
jupyter notebook --ip=$1 --notebook-dir=/home/pi --config=/home/pi/.jupyter/jupyter_notebook_config.py &

#### add this code !
python /home/pi/.ap/toggle_sw.py
####

bash /home/pi/.ap/toggle_ap_wifi.sh

exit 0
```

[hostapdとWifiClientの切り替え](https://hackmd.io/s/SyRtOEBce)を行った際に追加した`bash /home/pi/.ap/toggle_ap_wifi.sh`の上に記述します。


- - -

### 使い方
スイッチをONないしはOFFにした後に再起動をかけることで、任意のモード（AP or Wifi）にすることが出来ます。
