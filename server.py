import argparse
import sys
import logging
import project_logging.configs.config_log_server
from socket import *

from common.utils import get_message, send_message
from common.variables import DEFAULT_PORT, ACTION, TIME, USER, ACCOUNT_NAME, ERROR


logger_server = logging.getLogger('server')


def main():
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    listen_port = namespace.p
    listen_ip = namespace.a

    if listen_port < 1024 or listen_port > 65535:
        logger_server.critical(f'Номер порта {listen_port} должен быть в диапазоне от 1024 до 65535')
        sys.exit(1)
    logger_server.info(f'Сервер запущен: номер порта {listen_port}, адрес {listen_ip}')

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((listen_ip, listen_port))
    s.listen(5)

    while True:
        client, address = s.accept()
        message = get_message(client)
        logger_server.info(f'Получено сообщение от клиента: {message}')
        response = check_message(message)
        logger_server.info(f'Отправлен ответ клиенту: {response}')
        send_message(client, response)
        client.close()


def check_message(message):
    logger_server.debug(f'Проверка сообщения от клиента : {message}')
    if ACTION in message and message[ACTION] == 'presence' and TIME in message and USER in message and \
            message[USER][ACCOUNT_NAME] == 'Guest':
        return {'response': 200}
    return {
        'response': 400,
        ERROR: 'Bad Request'
    }


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    return parser


if __name__ == '__main__':
    main()
