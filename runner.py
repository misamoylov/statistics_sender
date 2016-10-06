# coding=utf-8
import ast
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
        # Step 2
        try:
            response = os.system("python D:\Python_Projects\statistics_sender\client.py")
            transport = paramiko.Transport((host['client']['@ip'], 22))
            transport.connect(username=host['client']['@username'],
                              password=host['client']['@password'])
            sftp = paramiko.SFTPClient.from_transport(transport)

            remotepath = '/tmp/client.py'
            localpath = '/home/msamoylov/statistics_sender/client.py'

            sftp.put(localpath, remotepath)

            ssh.connect(host['client']['@ip'],
                        username=host['client']['@username'],
                        password=host['client']['@password'])
        # Step 3
            stdin, stdout, stderr = ssh.exec_command('python /tmp/client.py')
            response = dict(ast.literal_eval(stdout.read()))
            srv.read_response_from_client(host['client']['@ip'], response)
            print(response)

            if response['cpu'] > host['client']['alert'][0]['@limit'].strip('%'):
                #send message to owner
                text = "cpu: raises limit, yours current cpu load in % {}".format(srv.decrypt(response['cpu']))
                srv.send_email(host['client']['@mail'], text)
            elif response['memory'] > host['client']['alert'][0]['@limit'].strip('%'):
                # send message to owner
                text = "memory: raises limit, yours current available memory in % {}".format(
                    srv.decrypt(response['memory']))
                srv.send_email(host['client']['@mail'], text)
            elif 'log_message' in response and response['log_message'] == 'yes':
                # send message to owner
                text = "You have high priority security events in logs".format(
                    response['log_message'])
                srv.send_email(host['client']['@mail'], text)
            ssh.close()
        except Exception as e:
            print("Cannot execute client script on remote host {}".format(host['client']['@ip']),
                  e)

main()
