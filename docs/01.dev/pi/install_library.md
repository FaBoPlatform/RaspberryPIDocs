# FaBo Pythonライブラリのインストール

## Overview

I2C BrickとSerialのBLE関連Brickにつきましては、簡単にご利用頂けるようPython用のライブラリを用意しております。

ご利用頂けるライブラリにつきましては、各Brickのページ、または下記のページから確認することができます。


PyPI

https://pypi.python.org/pypi?%3Aaction=search&term=FaBo&submit=search

なお、FaBoのライブラリにつきましては、pipコマンドによりインストールします。

## Pythonのバージョンについて

Pythonのライブラリは、RaspberryPiの初期状態でインストールされている2.7系に対応しています。

## インストール方法
ターミナルを起動し、以下のコマンドを実行します。（インストールするモジュール名を入力）

```
sudo pip install モジュール名
```

例：#201 3Axis i2c Brickのライブラリをインストールする場合
```
sudo pip install FaBo3Axis_ADXL345
```

これでインストール完了です。

## サンプルプログラムの実行

サンプルプログラムはGithubの各ライブラリのexampleフォルダに格納してありますので、git cloneコマンド等でファイルを取得して実行して下さい。

Github FaBoPlatform (python)

https://github.com/FaBoPlatform?utf8=%E2%9C%93&query=python

#### git cloneの例（#201 3axis i2c Brick)

```
git clone https://github.com/FaBoPlatform/FaBo3Axis-ADXL345-Python
```

exampleフォルダに移動してプログラム実行
```
cd FaBo3Axis-ADXL345-Python/example
python 3axis.py
```
