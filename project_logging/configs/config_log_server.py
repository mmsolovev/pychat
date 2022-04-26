import logging
import os
import sys
import logging.handlers

from common.variables import LOGGING_LEVEL

sys.path.append('../logs')


format_server = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, 'server.log')

crit_hand = logging.StreamHandler(sys.stderr)
crit_hand.setLevel(logging.ERROR)
crit_hand.setFormatter(format_server)
log_file = logging.handlers.TimedRotatingFileHandler(path, encoding='utf8', interval=1, when='D')
log_file.setFormatter(format_server)

app_log = logging.getLogger('server')
app_log.addHandler(crit_hand)
app_log.addHandler(log_file)
app_log.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    app_log.critical('Критическая ошибка')
    app_log.error('Ошибка')
    app_log.debug('Отладочная информация')
    app_log.info('Информационное сообщение')
