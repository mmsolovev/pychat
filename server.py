import sys
from socket import *
import time

from common.utils import get_message, send_message
from common.variables import DEFAULT_IP, DEFAULT_PORT, ENCODING, ACTION, TIME, USER, ACCOUNT_NAME, ERROR


def main():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
            if listen_port < 1024 or listen_port > 65535:
                raise ValueError
    except IndexError:
        listen_port = DEFAULT_PORT
    except ValueError:
        print('Номер порта должен быть в диапазоне от 1024 до 65535')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_ip = sys.argv[sys.argv.index('-a') + 1]
    except IndexError:
        listen_ip = ''

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((listen_ip, listen_port))
    s.listen(5)

    while True:
        client, address = s.accept()
        message = get_message(client)
        print(message)
        response = check_message(message)
        send_message(client, response)
        client.close()


def check_message(message):
    if ACTION in message and message[ACTION] == 'presence' and TIME in message and USER in message and \
            message[USER][ACCOUNT_NAME] == 'Guest':
        return {'response': 200}
    return {
        'response': 400,
        ERROR: 'Bad Request'
    }


if __name__ == '__main__':
    main()
