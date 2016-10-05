# coding=utf-8
import psutil
from uptime import uptime
import os
from Crypto.Cipher import AES
#http://www.blog.pythonlibrary.org/2010/07/27/pywin32-getting-windows-event-logs/
#http://code.activestate.com/recipes/577499-windows-event-log-viewer/
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
