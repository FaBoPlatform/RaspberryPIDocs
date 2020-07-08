# InfluxAPI

## データ書き込み用のWebAPI

データベースの作成

```shell
curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE webapidb"
```

```shell
urlencode "q=CREATE DATABASE webapidb"
HTTP/1.1 200 OK
Connection: close
Content-Type: application/json
Request-Id: 1f1643bc-ae13-11e7-801b-000000000000
X-Influxdb-Version: 1.3.5
Date: Tue, 10 Oct 2017 23:31:20 GMT
Transfer-Encoding: chunked

{"results":[{"statement_id":0}]}
```

```shell
curl -i -XPOST 'http://localhost:8086/write?db=webapidb' --data-binary 'aizu,temperature=11 humidity=30.1'
```

```shell
HTTP/1.1 204 No Content
Content-Type: application/json
Request-Id: 562d4f3e-ae13-11e7-801e-000000000000
X-Influxdb-Version: 1.3.5
Date: Tue, 10 Oct 2017 23:32:53 GMT
```

## データの読み込み

```shell
curl -G 'http://localhost:8086/query?pretty=true' --data-urlencode "db=webapidb" --data-urlencode "q=SELECT *  FROM \"aizu\""
```

```shell
{
    "results": [
        {
            "statement_id": 0,
            "series": [
                {
                    "name": "aizu",
                    "columns": [
                        "time",
                        "humidity",
                        "temperature"
                    ],
                    "values": [
                        [
                            "2017-10-10T23:32:53.151305504Z",
                            30.1,
                            "11"
                        ]
                    ]
                }
            ]
        }
    ]
}
```