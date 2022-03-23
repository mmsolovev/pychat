import argparse
import logging
import sys
import time
import project_logging.configs.config_log_client
from socket import *

from common.utils import send_message, get_message
from common.variables import DEFAULT_IP, DEFAULT_PORT, ACTION, TIME, USER, ACCOUNT_NAME, ERROR


logger_client = logging.getLogger('client')


def main():
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    server_ip = namespace.ip
    server_port = namespace.port

    if server_port < 1024 or server_port > 65535:
        logger_client.critical(f'Номер порта {server_port} должен быть в диапазоне от 1024 до 65535')
        sys.exit(1)
    logger_client.info(f'Клиент запущен: номер порта {server_port}, адрес {server_ip}')

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((server_ip, server_port))
    message = presence()
    send_message(s, message)
    answer = check_answer(get_message(s))
    logger_client.info(f'Получен ответ от сервера {answer}')
    print(answer)


def check_answer(message):
    logger_client.debug(f'Проверка сообщения от сервера: {message}')
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
    logger_client.info(f'Создано сообщение для пользователя {account_name}')
    return out


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip', default=DEFAULT_IP, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    return parser


if __name__ == '__main__':
    main()
