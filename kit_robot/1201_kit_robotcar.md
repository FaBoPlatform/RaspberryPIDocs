# #1201 Robot Car Kit for Arduino

<center>![](/img/kit/product/Robo.jpg)
<!--COLORME-->

## Overview
RobotCarKitは、Arduinoから制御できるロボットカーを簡単に作成することができるキットです。

## 部品一覧

###二輪駆動のロボカー用パーツリスト
![](/img/kit/manual/car_manual001.jpg)

1. Arduino本体（UNO）+ Arduinoケース（Fabo製。無くても可）
2. モーターシールド
3. 本体アクリル板
4. 9V電池ボックス＋後輪アジャスターアクリル板
5. 前輪アジャスターアクリル板
6. 電池ボックスアジャスターアクリル板
7. ギアードモーター（固定ネジ付き）
8. タイヤ
9. 単三電池ボックス（４本用）
10. 単三電池４本
11. 9V電池ケーブル
12. 9V電池
13. 25mmキャスター

###ネジ
![](/img/kit/manual/car_manual002.jpg)

ネジA. 単三電池ボックス固定用ネジ（２本）

ネジB. Arduino本体（３本）、前後輪固定ネジ（４本x２）

## 組み立て方法

### 1. 本体アクリルにArduino固定用ネジを取り付ける

![](/img/kit/manual/car_manual101.jpg)

本体アクリル板は三角孔がある方が前となります。
裏表に注意してください。写真は表です。

![](/img/kit/manual/car_namual102.jpg)

ネジBを先が上部に突き出るような形で裏側からネジを取り付けし、ナットで固定します。

![](/img/kit/manual/car_namual103.jpg)

Arduinoが上からハメ込める位置にネジが固定されているのを確認してください。
写真は裏から見た時のもの。
取り外しが容易にできる構図です。ナットでの固定はしません。

### 2.電池ボックスを取り付ける

![](/img/kit/manual/car_namual104.jpg)

裏側に単三電池ボックスを取り付けます。
ボックスと本体アクリル板の間に電池ボックスアジャスターアクリル板（パーツNo6）を挟むように、ネジAで固定します。
パーツNo6を挟まないと電池ボックスが斜めになります。
リード線は前方に向けて固定してください、

![](/img/kit/manual/car_namual105.jpg)

手順１の前に電池ボックスを取り付けると、Arduino固定ネジが取り付けられなくなるので注意してください。

<font color='#FF0000'>※この時点では単三電池は取り付けないでください。

### 3. 前輪を取り付ける

![](/img/kit/manual/car_namual106.jpg)

パーツ５（四角い穴が無い板）を３枚使います。ネジBを使います。

### 4.後輪を取り付ける

![](/img/kit/manual/car_namual107.jpg)

![](/img/kit/manual/car_namual108.jpg)

パーツ４（四角い穴が有る板）を４枚使います。ネジBを使います。
9V電池が入る事を確認してください。

### 5.ギアードモーターを取り付ける

![](/img/kit/manual/car_namual109.jpg)

本体アクリル板と固定する治具の方向とモーターの向きに注意してください。
取り付けたらタイヤも取り付けます。
裏側に取り付けた電池ボックスに干渉しない事を確認してください。

### 6. Arduinoにモーターシールドを取り付ける

![](/img/kit/manual/car_namual110.jpg)

![](/img/kit/manual/car_namual111.jpg)

Arduino本体の上にモーターシールドを亀の子状に取り付けます。
ピンソケットがズレないように注意してください。

### 7. リード線をつなげる

![](/img/kit/manual/car_namual112.jpg)

![](/img/kit/manual/car_namual113.jpg)

モーターシールドの電源と制御するギアードモーターの線をつなげます。
モーター側は線が反対でも問題ないですが（プログラムの変更で対応可能）、<font color='#FF0000'>電源側は電極を間違えると故障の原因になるので気をつけて下さい。

組み立ては以上となります。
電池は動作させる直前に取り付けます。

### 操作方法
操作方法につきましては、MotorShield for Arduinoの項目をご参照下さい。

* Motor Shield for Arduino

http://fabo.io/601.html
