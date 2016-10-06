import smtplib
import sqlite3
import xmltodict
import os
from cryptography.fernet import Fernet
import xml.etree.ElementTree as ET

from settings import CONFIG_PATH
response = {'host': '127.0.1.1', 'cpu': 'gAAAAABX9jSiPuEGkVKGqi8V7GY0VEFUCOuchv2EOvalOcC98y0P7GrMmdLAKmhZvhErE5LS5ub_7-TttxlSnOAyiqJihxXE9A==', 'os': 'gAAAAABX9jSiFHO9pJyxdhKc8iJ2gHExf4Jf43YhWMwCr0nr0PDYuwrNgxnViWAiZz13YeZVT63snh2Nm9oyQVHprSpQCeQUSw==', 'uptime': 'gAAAAABX9jSiH_X8_UdIIvhOtnbL9xX3i3vn3BdnnGqXXSSN3s6ob7Bz-ItlND2exJgztG2N33fJsP2gj4rGYDMwCyLMnqcNvteS6Nai9ZzMGjP_VdtYvwOH_Tjl_bqBB5jPRwtcw47SQQ9MkEEXI5VuMz3kl0Qj-rK2TyesxF6VX-1QmHI7BvSSKQJSwn8Kof-3YIcIAyHjUBTy_sgJKXAbMlvpc9PE3A==', 'memory': 'gAAAAABX9jSinuQfligXGzNBz0tYy7qzfSkH3Ux80eiNlBX9ZesfVG_UXSg8SDn-VimSMPfy-N67zzedwIm3D2YV-5Lo-Z8Q-w=='}

key = 'cpB2--8hBT7qbXjZW7QQwYolI6g39p96bslIVAMZ7kA='

class Server(object):
    def __init__(self, dbname):
        self.db = sqlite3.connect(dbname)
        self.cursor = self.db.cursor()
        self.fernet = Fernet(key)

    def smtp_sender(self, ):
        pass

    def selectall(self):
        self.cursor.execute('select * from hosts')
        return self.cursor.fetchall()

    def xml2db(self):
        return ET.parse('/home/msamoylov/statistics_sender/configs/user1.xml')

    def updatedb(self):
        for config in self.get_configs():
            self.cursor.execute('select ip_address from hosts where ip_address = ?', (
                config['client']['@ip'],))
            if len(self.cursor.fetchall()) == 0:
                self.cursor.execute('''INSERT INTO hosts(
            ip_address, os, user, password, mail, lim_mem, lim_cpu
            ) VALUES(?, ?, ?, ?, ?, ?, ?)''', (
                    config['client']['@ip'],
                    config['client']['@os'],
                    config['client']['@username'],
                    config['client']['@password'],
                    config['client']['@mail'],
                    config['client']['alert'][0]['@limit'].strip('%'),
                    config['client']['alert'][1]['@limit'].strip('%')))
                self.db.commit()

    def get_hosts(self):
        hosts = []
        configs = self.get_config_files()
        for config in configs:
            tree = ET.parse(CONFIG_PATH+config)
            root = tree.getroot()
            hosts.append(root.attrib['ip'])
        return hosts

    def get_config_files(self):
        return os.listdir(CONFIG_PATH)

    def get_configs(self):
        """

        :return: list of dicts with configs
        """
        config_files = self.get_config_files()
        conf = []
        for config in config_files:
            with open(CONFIG_PATH+config) as f:
                conf.append(xmltodict.parse(f.read()))
        return conf


    def read_response_from_client(self, response):
        """Decrypt response and update db

        :param response:
        :return:
        """
        pass

# a = Server('example.db')
# print(a.xml2db())
# for c in a.get_configs():
#     print(c)
# a.updatedb()
# print(a.selectall())
