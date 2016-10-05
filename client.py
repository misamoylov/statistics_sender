# coding=utf-8
import psutil
from uptime import uptime
import os
from Crypto.Cipher import AES

class Client(object):
    def __init__(self):
        self.cryptor = AES.new('key', AES.MODE_CBC, 'IV456')

    def get_host_info(self, Windows=False):

        def get_uptime():
            return self.cryptor.encrypt(str(uptime()))

        def get_mem():
            return str(psutil.virtual_memory().percent)

        def get_cpu():
            return str(psutil.cpu_percent())

        host_info = {'host': "",
                     'uptime': get_uptime(),
                     'memory': get_mem(),
                     'cpu': get_cpu(),
                     }
        return host_info
