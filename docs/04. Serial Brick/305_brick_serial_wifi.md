# #305 Wifi Serial Brick

[](../img/300_serial/product/305.jpg)
<!--COLORME-->

## Overview
Wifi通信ができるBrickです。

## 接続
Serialコネクタに接続します。
![](../img/300_serial/connect/305_wifi_connect.jpg)

## Support
|Arduino|
|:--:|
|◯|

## ESP-WROOM-02 Datasheet
|Document|
|--|
|[ESP-WROOM-02 Datasheet Page](https://espressif.com/en/products/hardware/esp-wroom-02/resources)|

## 回路図
![](../img/300_serial/schematic/305_wifi.png)



####ATコマンド（基本コマンド）

|  |コマンド名  | レスポンス |
| -- | -- | -- |
| テスト | AT | OK |
| ファームウェアのバーション表示 | AT+GMR | バーション表示 |
| コマンドエコー設定 | ATE1 | OK |

####ATコマンド(Wifiコマンド）

|  |コマンド名  | 正常レスポンス |
| -- | -- | -- |
| Wifiの設定 | AT+CWMODE | 1:ステーション2:アクセスポイント3:ステーション、アクセスポイント  例 AT+CWMODE=1|
| アクセスポイント一覧 | AT+CWLAP | SSID名,電波強度,Macアドレス,0:キーなし 2:WPA 3:WPA2  4:WPA_WPA2  |
| アクセスポイントに接続| AT+CWJAP="SSID名","パスワード" | WIFICONNECTED |

####ATコマンド(IPコマンド）

|  |コマンド名  | 正常レスポンス |
| -- | -- | -- |
| IPアドレスの確認 | AT+CIFSR | +CIFSR:STAIP,"IPアドレス"　+CIFSR:STAMAC,"Macアドレス"|
| TCPまたは、UDPコネクション開始 | AT+CIPSTART | CONNECT OK|
| データの送信 | AT+CIPSEND |OK　＞　が表示される|


##Wifiモジュールの動作確認
AT+CWMODE=1及びAT+CIFSRコマンドをArduinoのシリアルモニタから入力し、IPアドレス(例：192.168.10.8)を確認する。次にパソコンにターミナルからPingコマンドを実行する。

ping 192.168.10.8
64 bytes from 192.168.10.8: icmp_seq=3 ttl=255 time=6.434 ms
などのレスポンスが返ってきたら成功です。



## Sample Code
### for Arduino(サンプル１)
サンプル１は、Arduino IDEでコマンド入力できる。9600bpsでの通信。サンプル１は、Arduino IDEでコマンド入力できる。9600bpsでの通信。WifiモジュールはArduino（SoftSerial使用）においてデフォルトの通信速度は115200bpsなのでを9600bpsにする。サンプル２（9600bpsに設定）を実効後、サンプル１（コマンド入力可能）を実効してください。サンプル３でIoTプラットフォームであるIFTTTを使います。サンプル１を実行後、ArduinoIDEのシリアルモニタを開き、CL及びLF,9600bpsに設定する。シリアルモニタのテキストボックスにATコマンドを入力し送信ボタンかエンターキーでATコマンドが入力できます。ATと入力し、OKが返ってきたらシリアル通信は正常です。


```
//
// FaBo Brick Sample 1
// 2016/2/23
// Wifi Brick #305
#include <SoftwareSerial.h>

int bluetoothRx = 13;
int bluetoothTx = 12;

SoftwareSerial mySerial(bluetoothRx, bluetoothTx); // RX, TX

void setup()
{
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  Serial.println("Goodnight moon!");

  // set the data rate for the SoftwareSerial port
  mySerial.begin(9600);
}
int c = 0;
void loop() // run over and over
{
  if (mySerial.available()){
    char c = mySerial.read();
    Serial.write(c);

  }
  if (Serial.available())
    mySerial.write(Serial.read());
}
```

### for Arduino（サンプル２）

ArduinoUNOとWifiBruckとの通信はソフトウェアシリアル通信を行っています。115200bps（デフォルト）では文字化けしやすいので、＃305 Wifi BrickとArduinoShield間の通信速度を9600bpsに変更し、Ardunoとパソコン間のハードウェアシリアル通信は9600pbsとします。


```
//
// FaBo Brick Sample 2
// 2016/2/23
// Wifi Brick #305
// 115200bps→9600bps
#include <SoftwareSerial.h>
#define TimeInterval 2000
#define ComminucationSpeed_Arduino 9600
#define ComminucationSpeed_bleShield 115200

int bluetoothRx = 13;
int bluetoothTx = 12;

SoftwareSerial bleShield(bluetoothRx, bluetoothTx);



void setup()
{
  Serial.begin(ComminucationSpeed_Arduino);
  while (!Serial) {
  }

  Serial.println("bps changed!");

  // set the data rate for the SoftwareSerial port
  bleShield.begin(ComminucationSpeed_bleShield);
}

void ResposeCatch(){
  while(bleShield.available()){
  Serial.write(bleShield.read());
  bleShield.write(Serial.read());
   }
   delay(TimeInterval);
}

void loop()
{
  ResposeCatch();
   delay(TimeInterval);

   bleShield.println("AT+UART_DEF=9600,8,1,0,0");
   ResposeCatch();
   Serial.println("Excute");
   while(1){
    }

}
```

### for Arduino(サンプル３)
IFTTTを使い、Fabo#115Humidity Brickセンサーで取得したデータをMakerで受け、Googleドライブのスプレッドシートにレコードを追加します。#115Humidity BrickをA0に接続します。
##IFTTTのアカウント(SingUP)を作る。
IFTTTのWebサイトにアクセス。右上の画面にあるSingUPをクリックしてアカウントを作成。Welcome to IFTTTというメールが送られてくるので、Get Startedをクリックして登録完了。
##IFTTTのレシピを作成。
IFTTTに再びアクセスし、Thisを選択。Search ChannnelボックスにMakerで検索。create trigger画面が出る。Receive a web requestをクリックします。
Event Nameを入力　例：115_Humidityと入力します。
thatを選択。Choose Action Channel画面が出る。GoogleDriveで検索する。
GoogleDriveの許可を与える。(Googleアカウントがない方はアカウントを作ります。)
Choose an Actionの画面が出たら、”Add row to spredsheet"を選択。(１ファイル2000行まで記録できる。2000行を超えると別ファイルが生成される)
次に、Complete Action Fields画面が表示される。ファイル名、列の設定、パスの設定ができる。しかし、今回の例の場合は、何も変更しないでCreate Actionボタンを押す。
すると、Create and connect画面が現れ、レシピのタイトルが確認できる。確認ができたら、Create Recipeボタンを押す。
次に画面右上にあるChannelをクリックします。Makerで検索します。
Maker Channnel画面が出たら、クリックしkeyをコピーしてサンプルコードに貼り付けます。


サンプルコードに接続したいSSIDとWifiのパスワードを入力、Event NameとKeyを入力しコンパイルします。
GoogleDriveでIFTTTというフォルダができているので、クリックし任意のスプレッシートにデータが書き込まれているのか確認します。無事に書き込まれているなら成功です。

必要なライブラリは[#115Humidity Brick](http://www.fabo.io/115.html)を参考にしてください。


```
//
// FaBo Brick Sample 3(To transmit data to Google Drive at IFTTT.)
// 2016/7/21
// Wifi Brick #305
//Rev 0.0.0
#include <SoftwareSerial.h>
#include <ArduinoJson.h>
#include "DHT.h"

#define bluetoothRx   13
#define bluetoothTx   12

const String ssid     = "ssid";
const String password = "password";
const String Serverhost     = "maker.ifttt.com";
const int httpPort   = 80;
const String key = "key";
const String event = "event name";
const String uri     = "/trigger/" + event + "/with/key/" + key;
struct dht_Data {
  float h;
  float t;
  };

SoftwareSerial bleSheild(bluetoothRx, bluetoothTx);
DHT dht(A0, DHT11);
dht_Data dht_data;


void wifiConnect(){
  delay(100);
  bleSheild.begin(9600);
  delay(1000);
   //テストコマンド
  bleSheild.println("AT");
  delay(5000);
   if (!bleSheild.find("OK")) {
  Serial.println("ATisBad");
  return;
  }else{
    Serial.println("ATisOK");
    }
  //アクセスポイントに接続
  String cwjap = "AT+CWJAP=\"" + ssid + "\",\"" + password + "\"";
  Serial.println("AccessPointConnection.");
  bleSheild.println(cwjap);
  Serial.println(cwjap);
  delay(10000);
  if (!bleSheild.find("OK")) {
    }else{
      Serial.println("AT+CWJAPisOK");
      }
  //TCPプロコトルで接続
  String cipst = "AT+CIPSTART=\"TCP\",\"" + Serverhost + "\"," + httpPort;
  bleSheild.println(cipst);
  Serial.println(cipst);
  delay(50);
  if (!bleSheild.find("OK")) {
      Serial.println("AT+CIPSTARTisBad");
    }else{
      Serial.println("AT+CIPSTARTisOK");
      Serial.println("Wifi Connected");
      }
  }
//湿度、温度測る
void tmpMesurement(){
  dht_data.h = dht.readHumidity();
  dht_data.t = dht.readTemperature();
}

void setup()  {
  //ESP8266とシリアル通信
  bleSheild.begin(9600);
  //Arduinoのシリアル通信
  Serial.begin(9600);
  dht.begin();
  wifiConnect();

}
void loop() {
  String value;
  //２００文字分でバッファを用意。
  StaticJsonBuffer<200> jsBuffer;
  JsonObject& data = jsBuffer.createObject();
  if (!data.success()){
    Serial.println("createObject failed!");
    }
  tmpMesurement();
  data["value1"] =  dht_data.h;
  data["value2"] =  dht_data.t;
  data.printTo(value);
  value += "\r\n";
  //HTTP POST
  String jsonPacket = "POST " + uri + " HTTP/1.1\r\nHost: " + Serverhost + "\r\nContent-Length: " + value.length() + " \r\nContent-Type: application/json\r\n\r\n" + value +"\r\n";
  Serial.println(jsonPacket);
  //トランスペアレントモードで送信
  bleSheild.print("AT+CIPSEND=");
  bleSheild.println(jsonPacket.length());
  delay(10);
  if (!bleSheild.find(">")){
    Serial.println("AT+CIPSENDisBad");
  }
  //HTTPリクエスト送信
  Serial.println("Request.");
  bleSheild.print(jsonPacket);
  delay(10);
  if (!bleSheild.find("SEND OK\r\n")) {
    Serial.println("SEND FAILED");
    //失敗した時は再接続する。
    wifiConnect();
    Serial.println("Attmpt reconnection.");
  }else{
    Serial.println("send completely.");
    Serial.print("");
    }
  delay(5000);
}
```


## Parts
- ESP-WROOM-02
