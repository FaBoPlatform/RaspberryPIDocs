# Grafana

## Grafanaのインストール

```shell
sudo apt-get install apt-transport-https curl
curl https://bintray.com/user/downloadSubjectPublicKey?username=bintray | sudo apt-key add -
echo "deb https://dl.bintray.com/fg2it/deb jessie main" | sudo tee -a /etc/apt/sources.list.d/grafana.listsudo apt update
sudo apt-get update
sudo apt-get install grafana
sudo service grafana-server start
sudo update-rc.d grafana-server defaults
```

## 初期のID, Pass
admin, admin
