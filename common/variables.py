"""
Константы
"""

import logging


# Адреса
DEFAULT_IP = '127.0.0.1'
DEFAULT_PORT = 7777

# Кодировка
ENCODING = 'utf-8'

# Текущий уровень логирования
LOGGING_LEVEL = logging.DEBUG

# Ограничения
MAX_CONNECTIONS = 5
MAX_PACKAGE_LENGTH = 1024

# JIM
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
SENDER = 'from'
DESTINATION = 'to'
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'
EXIT = 'exit'

# Ответы
RESPONSE_200 = {RESPONSE: 200}
RESPONSE_400 = {
            RESPONSE: 400,
            ERROR: None
        }
