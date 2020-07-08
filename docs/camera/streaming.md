# mjpg-streamerを使用したカメラ制御

[mjpg-streamer](https://github.com/jacksonliam/mjpg-streamer)を利用してカメラの映像をストリーミング配信しwebブラウザから見られるようにします。

## 下準備
cmake libjpeg8-devのインストール
```
sudo apt-get install -y cmake libjpeg8-dev
```

## mjpg-streamerのダウンロードとコンパイル

```
git clone https://github.com/jacksonliam/mjpg-streamer
cd mjpg-streamer/mjpg-streamer-experimental
make
```

## mjpg-streamerの実行
### RaspberryPiのカメラを使用する
実行前にターミナル上で'sudo raspi-config'を実行し、カメラを有効化しておく。( 5 Interfacing Options -> P1 Camera -> Yes )  
実行してからWebブラウザで http://RaspberryPiのIP:8081/stream.html にアクセスするとカメラで撮影しているリアルタイムの映像が見られる。

```
./mjpg_streamer -i "input_raspicam.so -fps 30" -o "output_http.so -w ./www -p 8081"
```

### USB接続のWebカメラを使用する
実行してからWebブラウザで http://RaspberryPiのIP:8082/stream.html にアクセスするとカメラで撮影しているリアルタイムの映像が見られる。

```
./mjpg_streamer -i "input_uvc.so -f 30" -o "output_http.so -w ./www -p 8082"
```
