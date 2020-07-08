# 特定ワードを全検索

## 特定ワードを全検索

```shell
$ sudo find /etc -type f -print0 | xargs -0 grep '192.168.0.65'
```