import sqlite3
# IP_addr - 'string' ip address of host, primary key
# OS - string operating system
# User - username for auth
# Passowrd - password for auth
# Mail - string, mail for sending errors
# Last Average CPU - text
# Limit CPU - text
# Last Average Memory Av - text
# Limit Average Memory - text
# sec_log_events - text, can be yes or no

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE hosts
             (ip_address text primary key, OS text, user VARCHAR(100),
               password text, mail text,
               av_cpu text, lim_cpu text, av_mem text,
               lim_mem text, sec_log_events text, uptime text)''')
conn.commit()
conn.close()
