#-*- coding=utf-8 -*-
import paramiko



#创建SSH对象
ssh = paramiko.SSHClient()

#把要连接的机器添加到known_hosts文件中
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接服务器
ssh.connect(hostname='192.168.3.172', port=22, username='king7', password='1234567a')

cmd = 'cat /etc/shadow'
stdin, stdout, stderr = ssh.exec_command(cmd)

result = stdout.read()

if not result:
    result = stderr.read()
ssh.close()

print result.decode()