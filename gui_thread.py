import socket


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("192.168.1.1", 80))
        return True
    except OSError:
        pass
    return False

while True:
    print(is_connected())