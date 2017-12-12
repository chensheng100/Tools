import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #允许连接不在know_hosts文件中的主机
ssh.connect('192.168.50.128',22,'root','6300nm..')
flag = True
while flag:
    command = raw_input('Input your command:')
    if command == 'exit':
        flag = False
    stdin,stdout,stderr = ssh.exec_command(command)  #3个变量的顺序不可变
    print stdout.read()
ssh.close();   