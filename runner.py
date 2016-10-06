# coding=utf-8
import os
import paramiko
from server import Server
from client import Client

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
                text = "cpu: raises limit, yours current cpu load in % {}".format(response['cpu'])
                srv.send_email(host['client']['@mail'], text)
            elif response['memory'] > host['client']['alert'][0]['@limit'].strip('%'):
                # send message to owner
                text = "memory: raises limit, yours current available memory in % {}".format(
                    response['memory'])
                srv.send_email(host['client']['@mail'], text)
            elif 'log_message' in response and response['log_message'] == 'yes':
                # send message to owner
                text = "You have high priority security events in logs".format(
                    response['log_message'])
                srv.send_email(host['client']['@mail'], text)
            ssh.close()
        except:
            pass

main()