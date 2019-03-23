from socket import *
udpserversocket=socket(AF_INET,SOCK_DGRAM)
udpserversocket.bind(('192.168.3.77',3000))
while True:
	data,addr=udpserversocket.recvfrom(2048)
	print addr,':',data
	buffer=raw_input('Response:')
	udpserversocket.sendto(buffer,(addr))
	if 'exit' in buffer : break
udpserversocket.close()
