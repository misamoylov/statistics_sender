import smtplib
import sqlite3
import os
import xml.etree.ElementTree as ET

from settings import CONFIG_PATH

class Server(object):
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()

    def smtp_sender(self, ):
        pass

    def xml2db(self):
        return ET.parse('/home/msamoylov/statistics_sender/configs/user1.xml')

    def get_hosts(self, configs):
        hosts = []
        for config in configs:
            tree = ET.parse(CONFIG_PATH+config)
            root = tree.getroot()
            return root.attrib['ip']


    def get_configs(self):
        return os.listdir(CONFIG_PATH)

    def resp2db(self, response):
        pass

a = Server('example.db')
print(a.xml2db())





>> import xml.etree.ElementTree as ET

>>> tree = ET.parse('/home/msamoylov/statistics_sender/configs/user1.xml')
>>> root = tree.getroot()
>>> root.tag
'client'
>>> root.attrib
{'username': 'user', 'mail': 'asa@asda.com', 'ip': '127.0.0.1', 'password': 'password', 'os': 'windows', 'port': '22'}

>>> import sqlite3
>>> conn = sqlite3.connect('example.db')

>>> c = conn.cursor()

>>> c.execute('''CREATE TABLE hosts
             (id integer primary key,
              ip_address VARCHAR(16), OS text, user VARCHAR(100),
               password real, mail text,
               av_cpu integer, lim_cpu integer, av_mem integer,
               lim_mem integer, last_sec_log_event text, uptime integer)''')
>>> conn.commit()

>>> c.execute('''INSERT INTO hosts(ip_address, os, user, password, mail, lim_cpu, lim_mem) VALUES('127.0.0.1, 'windows', 'Administrator', 'TestRoot!', 'asa@asda.com, 50, 50')''')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
OperationalError: near "windows": syntax error
>>> c.execute('''INSERT INTO hosts(ip_address, os, user, password, mail, lim_cpu, lim_mem) VALUES('127.0.0.1', 'windows', 'Administrator', 'TestRoot!', 'asa@asda.com, 50, 50')''')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
OperationalError: 5 values for 7 columns
>>> c.execute('''INSERT INTO hosts(ip_address, os, user, password, mail, lim_cpu, lim_mem) VALUES('127.0.0.1', 'windows', 'Administrator', 'TestRoot!', 'asa@asda.com', 50, 50)''')
<sqlite3.Cursor object at 0x7f44b78cff10>
>>> c.commit()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'sqlite3.Cursor' object has no attribute 'commit'
>>> conn.commit()
>>>
>>> c.execute('''SELECT * from hosts;''')
<sqlite3.Cursor object at 0x7f44b78cff10>
>>> print(c.fetchall())
[(1, u'127.0.0.1', u'windows', u'Administrator', u'TestRoot!', u'asa@asda.com', None, 50, None, 50, None, None)]