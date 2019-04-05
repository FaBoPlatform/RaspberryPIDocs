# -*- coding: utf-8 -*-

import bluetooth
import sys

try:
    server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    server_sock.bind(("",22))
except Exception as e:
    print(e)
    server_sock.close()
    sys.exit(0)

server_sock.listen(1)

# その後、Macの設定->Bluetoothに上記の名前が表示されるので、ペアリングする
client_sock, address = server_sock.accept()
print("Accepted connection from ",address)

while(True):
    data = client_sock.recv(1024)
    print("received [%s]" % data)
    if data == b'\r':
        break

client_sock.close()
server_sock.close()
