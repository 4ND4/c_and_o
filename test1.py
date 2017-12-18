import socket

from datetime import datetime
from time import sleep


def with_ping(hostname):
    import os
    return True if os.system("ping -c 1 " + hostname) is 0 else False


def with_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('8.8.8.8', 80))

    if result == 0:
        return True
    else:
        return False


while True:
    if with_ping('google.com'):
        print('connected')
    else:
        print('offline')

    sleep(2)
