# coding=utf-8
import pathos
from server import Server

def main():
    srv = Server('example.db')
    for host in srv.get_hosts():

        #1. Сервер читает конфиги по очереди и кладет их в базу, если такого пользователя еще нет (проверка по ip адресу)

        # Выполнение скрипта на удаленном хосте
        c = pathos.core.copy('client.py', destination='{}:~/hello.py'.format(address))
        s = pathos.core.execute('python client.py', host=address)
        print(s.response())
        #checker for response for address in db (request to db and check limits) and send mail if needed
