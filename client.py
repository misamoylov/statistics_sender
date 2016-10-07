# coding=utf-8
import psutil
import platform
import win32evtlog

from cryptography.fernet import Fernet
from uptime import uptime
key = 'cpB2--8hBT7qbXjZW7QQwYolI6g39p96bslIVAMZ7kA='

class Client(object):
    # just for example

    def __init__(self):
        self.fernet = Fernet(key)
        self.security_events_ids = ['4771', '675', '676', '4768']
        self.win_server = 'localhost'
        self.logtype = 'System'

    def check_windows_security_events(self):
        """ Check windows security events, if in windows logs some security events returns 'yes'
        :return: str 'yes' or 'no
        """
        hand = win32evtlog.OpenEventLog(self.win_server, self.logtype)
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        answer = 'no'
        for event in events:
            if event.EventID in self.security_events_ids:
                answer = 'yes'
                break
            else:
                return answer
        return answer

    def get_host_info(self):
        """

        :return: dict, dict with strings with host information: uptime, cpu, available memeory
        """

        def get_uptime():
            return str(uptime())

        def get_mem():
            return str(psutil.virtual_memory().percent)

        def get_cpu():
            return str(psutil.cpu_percent())

        if platform.system() is 'Windows':
            host_info = {"uptime": self.fernet.encrypt(get_uptime()),
                         "memory": self.fernet.encrypt(get_mem()),
                         "cpu": self.fernet.encrypt(get_cpu()),
                         "os": self.fernet.encrypt(platform.system()),
                         "log_message": self.fernet.encrypt(self.check_windows_security_events())
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