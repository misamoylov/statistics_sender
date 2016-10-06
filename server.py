import os
import smtplib
import sqlite3
import xmltodict
import xml.etree.ElementTree as ET

from cryptography.fernet import Fernet

from settings import CONFIG_PATH
from settings import FERNET_KEY
from settings import MAIL_LOGIN
from settings import MAIL_PASSWORD


class Server(object):
    def __init__(self, dbname):
        self.db = sqlite3.connect(dbname)
        self.cursor = self.db.cursor()
        self.fernet = Fernet(FERNET_KEY)
        self.smtp = smtplib.SMTP('smtp.gmail.com', 587)
        self.smtp.starttls()
        self.smtp.login(MAIL_LOGIN, MAIL_PASSWORD)

    def send_email(self, reciever, text):
        message = '''From: {}
         Subject: Yours computer have problems

         Yours computer have problems with {}'''.format(MAIL_LOGIN, text)
        self.smtp.sendmail(MAIL_LOGIN, reciever, message)

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

    def decrypt(self, text):
        return self.fernet.decrypt(text)

    def read_response_from_client(self, host, response):
        """Decrypt response and update db


        :param response: dict with params
        :return:
        """
        if 'log_message' in response:
            self.cursor.execute(
                """UPDATE hosts SET av_cpu = ? ,av_mem = ?,
                 uptime = ?, log_message = ? WHERE ip_address = ? """,
                (self.fernet.decrypt(response['cpu']),
                 self.fernet.decrypt(response['memory']),
                 self.fernet.decrypt(response['uptime']),
                 self.fernet.decrypt(response['log_message']),
                 host))
        elif 'log_message' not in response:
            self.cursor.execute(
                """UPDATE hosts SET av_cpu = ? ,av_mem = ?,
                 uptime = ? WHERE ip_address = ? """,
                (self.fernet.decrypt(response['cpu']),
                 self.fernet.decrypt(response['memory']),
                 self.fernet.decrypt(response['uptime']),
                 host))
        else:
            return "Bad response format"

# a = Server('example.db')
# # print(a.xml2db())
# # for c in a.get_configs():
# #     print(c)
# a.updatedb()
# # print(a.selectall())
# response = {'host': '127.0.1.1', 'cpu': 'gAAAAABX9kj4aDBtpEBLhvlFdxFqwHAbVKtSyfEbObog5MX1lwMz3q1K1xaVFnzU_2S3r6BsVDD-9inr-5CYHZjDhk_m5EIuZw==', 'os': 'gAAAAABX9kj4EI-ITQgUyuAJDdbdm4zNcWIysXbItjZHfpq4PAn8JqNgu1rcmdY4CG_2MY9V_7o0oN1QLV7i1AAcWN66dNmlmg==', 'uptime': 'gAAAAABX9kj4abZ0xAqgYwgUKARYG0natcGnnoMoCGOvOurk2WtgWyggcytUrywtfLcu1cfEA3a0rN-b_kIWGbbtzD3kSyvnhw==', 'memory': 'gAAAAABX9kj4kZL0mRPUcnOopj3Uw2bezZMfdnFfr-JRys9zUo1yCs_LLp-_svidqMFVwHttPwIiKI-ttbTV9BVQnRoCfdFFQw=='}
#
# a.read_response_from_client(response)
# print(a.selectall())
