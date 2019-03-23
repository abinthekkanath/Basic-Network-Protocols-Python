from socket import *
udpclientsocket=socket(AF_INET,SOCK_DGRAM)
while True:
	data=raw_input('Message:')
	udpclientsocket.sendto(data,('192.168,3,77',80000))
	buffer,addr=udpclientsocket.recvfrom(2048)
	print addr,':' buffer
	if 'exit' in buffer:break
	
udpserversocket.close()
	
