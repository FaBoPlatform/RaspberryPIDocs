# Influxdb

## Influxdbのインストール

InfluxdbのRepoからソースを取得

```shell
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
```

パッケージをUpdateし、influxdbをインストール

```shell
sudo apt update
sudo apt -y install influxdb
```

## Influxdbの起動

influxdbを起動

```shell
sudo service influxdb start
```

動作の確認

```shell
ss -nlp | grep 808
```

8088, 8086を確認できれば動作OK

```shell
tcp    LISTEN     0      128    127.0.0.1:8088                  *:*                  
tcp    LISTEN     0      128      :::8086                 :::*     
```

## Influxdbへのアクセス

コマンドで接続

```shell
influx -precision rfc3339
InfluxDB shell version: 1.3.5
> 
```
Databaseを作成

```shell
> CREATE DATABASE testdb
```

Database情報を表示

```shell
> SHOW DATABASES
name: databases
name
----
_internal
testdb
```

Database使用を宣言

```shell
> USE testdb
Using database testdb
```

Tableの作成とデータのInsert

```shell
INSERT aizu,temperature=10.1 humidity=30.5
```

```shell
> SELECT * FROM aizu
name: aizu
time                           humidity temperature
----                           -------- -----------
2017-10-10T23:25:06.758717402Z 30.5     10.1
```



## 
