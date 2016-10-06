# coding=utf-8
import psutil
import platform


from cryptography.fernet import Fernet
from uptime import uptime

key = 'cpB2--8hBT7qbXjZW7QQwYolI6g39p96bslIVAMZ7kA='


class Client(object):

    def __init__(self):
        self.fernet = Fernet(key)

    def check_windows_security_events(self):
        """ Check windows security events
        :return: str 'yes' or 'no
        """

    def get_host_info(self):

        def get_uptime():
            return str(uptime())

        def get_mem():
            return str(psutil.virtual_memory().percent)

        def get_cpu():
            return str(psutil.cpu_percent())

        if platform.system is 'Windows':
            host_info = {"uptime": self.fernet.encrypt(get_uptime()),
                         "memory": self.fernet.encrypt(get_mem()),
                         "cpu": self.fernet.encrypt(get_cpu()),
                         "os": self.fernet.encrypt(platform.system()),
                         "log_message": ""
                         }
        else:
            host_info = {"uptime": self.fernet.encrypt(get_uptime()),
                         "memory": self.fernet.encrypt(get_mem()),
                         "cpu": self.fernet.encrypt(get_cpu()),
                         "os": self.fernet.encrypt(platform.system())
                         }
        return host_info

a = Client()
print(a.get_host_info())