from socket import *
import time
from common.variables import DEFAULT_IP, DEFAULT_PORT, ENCODING


s = socket(AF_INET, SOCK_STREAM)
s.bind((DEFAULT_IP, DEFAULT_PORT))
s.listen(5)

while True:
    client, addr = s.accept()
    data = client.recv(1000000)
    print('Сообщение: ', data.decode(ENCODING), ', было отправлено клиентом: ', addr)
    msg = 'Привет, клиент'
    client.send(msg.encode(ENCODING))
    client.close()
