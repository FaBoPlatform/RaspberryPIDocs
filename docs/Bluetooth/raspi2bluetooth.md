# Raspberry piとBluetooth接続をして通信をする

Raspberry piとMacなどをBluetoothを接続して，ターミナル上から文字を送る方法．


使用するソフトはMacなどではterminal上でscreenを使ったり，Arduino IDE付属のシリアルモニタを使用する．Windowsを使う場合はArduino IDEを使う方法が簡単かつ信頼できる方法である．

### 方法

1. Raspberry piはSDP(Bluetoothプロトコルの一つ)が動いていないので動かせるようにファイルを書き換える．`/etc/systemd/system/dbus-org.bluez.service`に設定ファイルがあるので，su権限を使ってファイルを書き換える．

```
ExecStart=/usr/lib/bluetooth/bluetoothd
```
　　この表記がされている部分を下のように書き換え．
  ```
  ExecStart=/usr/lib/bluetooth/bluetoothd --compat
  ```
  
 これにより互換モード(compat mode)になり，互換性を持ったbluetoothの運用が可能になる．
     
2.ラズパイのデバイス名を設定し検出可能に設定,かぶると識別できなくなるので，ユニークに設定する．

```
sudo hciconfig hci0 name 'hoge'
sudo hciconfig set class 0x4e2100
sudo hciconfig hci0 piscan
```
`0x4e2100`について
これはBluetoothのデバイスが,どのようなタイプの機器かを示す24ビットの値のことです．このアドレスの設定次第でスマートフォンやPCだということが他の機器に示されます．(Bluetoothの設定パラメータ Class of Device（CoD）というもの)

設定は色々と存在し，組み合わせで値が決まるので，[インターネット上でパラメーターを確認できるサイト](http://bluetooth-pentest.narod.ru/software/bluetooth_class_of_device-service_generator.html)がある．　

例![](https://i.imgur.com/p91yvcw.png)

`sudo hciconfig hci0 piscan`は，他の機器でこのデバイスがペアリングできるように設定できるコマンドである．

3. ペアリングが可能になるので，PCとRaspberry piを接続する．

2まで行ってもまだRaspberry piとPCの接続はできないので，以下のコマンドを実行する必要がある．

```
import bluetooth
import sys

try:
    server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    server_sock.bind(("",22))
except Exception as e:
    print(e)
    server_sock.close()
    sys.exit(0)
    
server_sock.listen(1)

bluetooth.advertise_service(server_sock, "TestService",
                     service_classes=[bluetooth.SERIAL_PORT_CLASS],
                     profiles=[bluetooth.SERIAL_PORT_PROFILE])
```

これを行うと設定画面からRaspberry piが認識され，きちんと接続できるようになる．

これで接続が完了した．

### 実際に通信を行い，文字を送信する．

(ここではPC側の操作になります．)

1. terminal上で`ls /dev/tty.*`を実行し，接続先のポートを確認する．

このコマンドで，現在接続されているポートを確認できる，特別に設定していなければ，`/dev/tty.hoge`などの先ほど設定したデバイス名になっている．

2. `screen`コマンドで事前に確認したデバイスに接続する．
接続したいデバイスを `ls /dev/tty.*` で確認したので，そのデバイスをscreenコマンドで`screen /dev/tty.hoge`として接続．

3. Raspberry piでサーバーと接続する
Raspberry piでサーバーを起動するプログラムを実行．これによってPC側でタイピングをした文字が，Raspberry pi上のterminalで表示される．

```
import bluetooth
import sys

try:
    server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    server_sock.bind(("",22))
except Exception as e:
    print(e)
    server_sock.close()
    sys.exit(0)
    
server_sock.listen(1)

# その後、Macの設定->Bluetoothに上記の名前が表示されるので、ペアリングする
client_sock, address = server_sock.accept()
print("Accepted connection from ",address)

while(True):
    data = client_sock.recv(1024)
    print("received [%s]" % data)
    if data == b'\r':
        break

client_sock.close()
server_sock.close()
```

終了の際は Enterキーを押すと終了する．

#### Arduino IDEを使用する方法．
Arduino IDEを使う際も，screenを使用する方法と手順は変わらない．上の`screen /dev./tty.hoge`で接続した後，Arduino IDEを起動して 9600bpsで接続，文字列などを入力し，送信するとRaspberry piに送信されて，screenを使用した時のように画面に表示される．