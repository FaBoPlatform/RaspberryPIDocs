# JupyterのService化

## Systemd

`/etc/sysyemd/system`以下に、jupyter.serviceを作成する。

`/etc/sysyemd/system/jupyter.service`

```shell
[Unit]
Description = Jupyter Notebook

[Service]
PIDFile=/var/run/jupyter.pid
ExecStart=/usr/local/bin/jupyter-notebook --ip= --config=/home/pi/.jupyter/jupyter_notebook_config.py
User=pi
Group=pi
Restart=always
RestartSec=10
WorkingDirectory=/home/pi/Documents
Type=simple

[Install]
WantedBy=multi-user.target
```

## 設定の確認

```shell
$ systemctl list-unit-files --type=service | grep jupyter
jupyter.service       invalid
```

## Serviceの起動　

```shell
$ sudo systemctl enable jupyter
```
