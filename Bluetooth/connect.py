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

bluetooth.advertise_service(server_sock, "TestService",
                     service_classes=[bluetooth.SERIAL_PORT_CLASS],
                     profiles=[bluetooth.SERIAL_PORT_PROFILE])
