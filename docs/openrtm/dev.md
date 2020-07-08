# OpenRTMをJupyerから操作する

## OpenRTMのインストール

OpenRTMの環境は、apt-getをつかって構築する。まず、apt-getの参照先Repoにopenrtmを追加する。

/etc/apt/sources.listの最後の行に、下記を追加する。

```shell
$ sudo vi /etc/apt/sources.list
```

```shell
...
deb http://openrtm.org/pub/Linux/raspbian/ jessie main
```

```shell
$ apt-get update
```
Updateする事で、apt-getにopenrtmのRepoが追加されるので、下記パッケージをインストールする。

```shell
$ apt-get -y --force-yes install gcc g++ make uuid-dev
$ apt-get -y --force-yes install libomniorb4-dev omniidl omniorb-nameserver
$ apt-get -y --force-yes install openrtm-aist openrtm-aist-dev openrtm-aist-example
$ apt-get -y --force-yes install openrtm-aist-python openrtm-aist-python-example
```

## ネームサーバの起動確認

omniNamesは、CORBAのネーミングサービス。omniorb-nameserverをインストールするとデーモンとして立ち上がる。

```shell
$ ps ax | grep omni
```

でプロセスが確認できれば、omniNamesが正常に起動している。

## 開発環境からネームサーバを参照

RaspberryPIのIPアドレスをメモし、開発環境からIPアドレスを指定して、CORBAのネーミングサービスに接続する。

