import logging
import os
import sys
import logging.handlers
sys.path.append('../logs/')


format_client = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, 'client.log')

crit_hand = logging.StreamHandler(sys.stderr)
crit_hand.setLevel(logging.ERROR)
crit_hand.setFormatter(format_client)
log_file = logging.FileHandler(path, encoding='utf8')
log_file.setFormatter(format_client)

app_log = logging.getLogger('client')
app_log.addHandler(crit_hand)
app_log.addHandler(log_file)
app_log.setLevel(logging.DEBUG)

if __name__ == '__main__':
    app_log.critical('Критическая ошибка')
    app_log.error('Ошибка')
    app_log.debug('Отладочная информация')
    app_log.info('Информационное сообщение')
