# coding=utf-8
import os
import paramiko
from server import Server

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def main():
    srv = Server('example.db')
    for host in srv.get_configs():
        """ Steps
        1. Read configs from xml and if config not in db update db
        2. Upload client script to remote host , if cannot pass,
         we need to have sftp server on remote machine
        3. Run client script on remote host

        """
        # Step 1
        srv.updatedb()
        print(srv.selectall())
        # Step 2
        try:
            print(os.system("python /home/msamoylov/statistics_sender/client.py"))

            # ssh.connect(host['client']['@ip'],
            #             username=host['client']['@username'],
            #             password=host['client']['@password'])
            # sftp = ssh.open_sftp()
            # sftp.put(os.path.split(os.path.abspath('client.py')), '/tmp/client.py')
            # sftp.close()
        # Step 3
            stdout = ssh.exec_command('python /tmp/client.py')[1]
            response = {}

            if response['cpu'] > host['client']['alert'][0]['@limit'].strip('%'):
                #send message to owner
                pass
            elif response['memory'] > host['client']['alert'][0]['@limit'].strip('%'):
                #send maessage
                pass
            elif 'log_message' in response:
                pass
            ssh.close()
        except:
            pass

main()