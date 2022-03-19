import sys
import time
from socket import *

from common.utils import send_message, get_message
from common.variables import DEFAULT_IP, DEFAULT_PORT, ACTION, TIME, USER, ACCOUNT_NAME, ERROR


def main():
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
    message = presence()
    send_message(s, message)
    answer = check_answer(get_message(s))
    print(answer)


def check_answer(message):

    if 'response' in message:
        if message['response'] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def presence(account_name='Guest'):
    out = {
        ACTION: 'presence',
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


if __name__ == '__main__':
    main()
