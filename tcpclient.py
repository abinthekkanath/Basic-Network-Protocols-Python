from socket import *
tcpclient=socket(AF_INET,SOCK_STREAM)
tcpclient.connect(('192.168.3.77',50000))
while True:
	data=raw_input("Message")
	tcpclient.send(data)
	buffer=tcpclient.recv(2048)
	print 'Remote:',buffer
	if 'EXIT' in buffer :break 
tcpclient.close()
