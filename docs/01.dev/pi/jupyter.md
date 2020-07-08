# Jupyter

## PIPのインストール

```shell
$ sudo apt-get install python-dev
$ sudo wget https://bootstrap.pypa.io/get-pip.py
$ sudo python ./get-pip.py
```

* `sudo apt-get install python-pip`ではうまくpipがインストールできない。

## Jupyterのインストール

```shell
$ sudo pip install jupyter
```

30分ほど時間がかかります。

## 他の便利なライブラリのインストール

```shell
$ sudo pip install panda numpy
```

10分ほど時間がかかります。

```shell
$ sudo apt-get install python-matplotlib
```

Matplot libでは、SWAPが必要になるので

swap停止

```shell
$ sudo /etc/init.d/dphys-swapfile stop
```
swap増加

```shell
$ sudo vi /etc/dphys-swapfile
```

`/etc/dphys-swapfile`

```
CONF_SWAPSIZE=1024
```

swap起動

```shell
$ sudo /etc/init.d/dphys-swapfile start
$ reboot
```

## 固定Tokenの作成

```
$ jupyter notebook --generate-config
```

```
$ vi ~/.jupyter/jupyter_notebook_config.py
```

c.NotebookApp.tokenのコメントアウトを消し、任意のTokenを指定する。(今回はfaboと指定)

`~/.jupyter/jupyter_notebook_config.py`
```
## Token used for authenticating first-time connections to the server.
#
#  When no password is enabled, the default is to generate a new, random token.
#
#  Setting to an empty string disables authentication altogether, which is NOT
#  RECOMMENDED.
c.NotebookApp.token = 'fabo'
```

## Jupyterの起動

```shell
$ jupyter-notebook --ip= --config=/home/pi/.jupyter/jupyter_notebook_config.py
```

```shell
$ ifconfig -a
```

RaspberryPIのIPアドレスを確認し、自分のマシンのブラウザから

> http://192.168.x.x:8888/

8888番ポートに接続する。

