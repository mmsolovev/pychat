import sys
from socket import *
from common.variables import DEFAULT_IP, DEFAULT_PORT, ENCODING


def main():
    """

    """

    try:
        server_ip = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_ip = DEFAULT_IP
        server_port = DEFAULT_PORT
    except ValueError:
        print('Номер порта должен быть в диапазоне от 1024 до 65535')
        sys.exit(1)

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((server_ip, server_port))
    msg = 'Привет, сервер'
    s.send(msg.encode(ENCODING))
    data = s.recv(1000000)
    print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной ', len(data), ' байт')
    s.close()


main()