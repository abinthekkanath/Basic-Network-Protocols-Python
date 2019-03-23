from socket import *
tcpserversocket=socket(AF_INET,SOCK_STREAM)
tcpserversocket.bind(('192.168.3.77',50000))
tcpserversocket.listen(5)
clientconnection,clientaddress=tcpserversocket.accept()
while True:
	data=clientconnection.recv(1024)
	print clientaddress,' ',data
	clientconnection.send(data.upper())
	print "Response:",data.upper()

	if 'exit' in data:break
clientconnection.close()
tcpserversocket.close()
