import sqlite3
# id - Integer, host id
# IP_addr - 'string' ip address of host
# User - username for auth
# Passowrd - password for auth
# Mail - string, mail for sending errors
# Last Average CPU - Integer
# Limit CPU - Integer
# Last Average Memory Av - Integer
# Limit Average Memory - Integer


conn = sqlite3.connect('example.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE hosts
             (id integer primary key,
              ip_address VARCHAR(16), user VARCHAR(100),
               password real, mail text,
               av_cpu integer, lim_cpu integer, av_mem integer,
               lim_mem integer, last_sec_log_event text)''')
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
