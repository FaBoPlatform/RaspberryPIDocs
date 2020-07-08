# カメラ

## PiCameraの接続

![](../img/camera/picam001.png)

## PiCameraを有効にする

```shell
$ sudo raspi-config
```

でCameraをEnableにする

## PiCameraの動作確認

```shell
$ vcgencmd get_camera
```

|値|意味|
|:--|:--|
|supported=0 detected=0|カメラが有効になっていない状態で、カメラが認識できない|
|supported=1 detected=0|カメラが有効になっている状態で、カメラが認識できない|
|supported=0 detected=1|カメラが有効になっていない状態で、カメラが認識できている|
|supported=1 detected=1|カメラが有効になっている状態で、カメラが認識できている|


supported=1 detected=1になっていれば、動作する。

## Jupyterで10行でデジカメを作る

```python
import RPi.GPIO as GPIO
import picamera

BUTTONPIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTONPIN, GPIO.IN)

camera = picamera.PiCamera()
camera.start_preview(alpha=255)

try:
    while True:
        if( GPIO.input(BUTTONPIN)): camera.capture("test.jpg")
except KeyboardInterrupt:
    camera.stop_preview()
    camera.close()
```

## トラブルシューティング

* Minimum GPU Memory
最低32MのGPUで、奨励128MのGPU

### Camera not working at all
下記のエラーに遭遇した場合の対処

> Example error message: "mmal: mmal_vc_component_create: failed to create component 'vc.ril.camera' (1:ENOMEM)"

* flexケーブルが、ちゃんと正しい方向に刺さっているか確認する。
* タブエンゲージがしまっているか確認する。
* 電流が十分か確認する。RPi + cameraでビデオ撮影すると260mAの電流が必要。Model Bは、RPi単体で550mAの電流を消費するので、カメラが追加されると800mA消費する。
* カメラの先の"PCM8M-SY101-A"と印字されているケーブルコネクタが離れている事があるので、その場合は上から押し込む。
* 上記のエラーは、"sudo raspi-config"でカメラを有効にしていない場合も発生する。
* PiCameraは、静電気やショートなど弱いため、十分に注意し扱うようにする。