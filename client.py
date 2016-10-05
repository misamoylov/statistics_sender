# coding=utf-8
import psutil
import platform
import socket
from uptime import uptime
import os
from Crypto.Cipher import AES
#http://www.blog.pythonlibrary.org/2010/07/27/pywin32-getting-windows-event-logs/
#http://code.activestate.com/recipes/577499-windows-event-log-viewer/
class Client(object):
    def __init__(self):
        self.cryptor = AES.new('key', AES.MODE_CBC, 'IV456')

    def get_host_info(self):


        def get_uptime():
            return self.cryptor.encrypt(str(uptime()))

        def get_mem():
            return str(psutil.virtual_memory().percent)

        def get_cpu():
            return str(psutil.cpu_percent())

        if platform.system() is 'Windows':
            host_info = {'host': self.cryptor.encrypt(socket.gethostbyname(socket.gethostname())),
                         'uptime': self.cryptor.encrypt(get_uptime()),
                         'memory': self.cryptor.encrypt(get_mem()),
                         'cpu': self.cryptor.encrypt(get_cpu()),
                         'os': self.cryptor.encrypt(platform.system()),
                         'logs': ""
                         }
        else:
            host_info = {'host': self.cryptor.encrypt(socket.gethostbyname(socket.gethostname())),
                         'uptime': self.cryptor.encrypt(get_uptime()),
                         'memory': self.cryptor.encrypt(get_mem()),
                         'cpu': self.cryptor.encrypt(get_cpu()),
                         'os': self.cryptor.encrypt(platform.system())
                         }
        return host_info

client = Client()
client.get_host_info()
