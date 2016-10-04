import sqlite3
# IP_addr - 'string' ip address of host, primary key
# OS - string operating system
# User - username for auth
# Passowrd - password for auth
# Mail - string, mail for sending errors
# Last Average CPU - Integer
# Limit CPU - Integer
# Last Average Memory Av - Integer
# Limit Average Memory - Integer


conn = sqlite3.connect('example3.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE hosts
             (ip_address text primary key, OS text, user VARCHAR(100),
               password text, mail text,
               av_cpu text, lim_cpu text, av_mem text,
               lim_mem text, last_sec_log_event text, uptime text)''')
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


conn = sqlite3.connect('example2.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE hosts
             (id integer not null,
              ip_address text not null, OS text, user VARCHAR(100),
               password text, mail text,
               av_cpu text, lim_cpu text, av_mem text,
               lim_mem text, last_sec_log_event text, uptime text, PRIMARY KEY (id, ip_address)''')
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()