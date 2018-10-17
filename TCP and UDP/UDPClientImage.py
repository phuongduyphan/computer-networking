from socket import *

serverName = '127.0.0.1'
serverPort = 12000

#IPv4, UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Different from TCP, in UDP, each packet maximum size is 65,507 bytes so
# the data of the image need to be divided into many packets
with open('music.jpg') as file:
	# read the first 1024 bytes from image file
	bytesToSend = file.read(1024)
	clientSocket.sendto(bytesToSend, (serverName, serverPort))
	# continue to read the next 1024 bytes from image file until nothing
	# remaining
	while bytesToSend:
		bytesToSend = file.read(1024)
		# eacth time send 1024 bytes of data image to the server
		clientSocket.sendto(bytesToSend, (serverName, serverPort))
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
		print(modifiedMessage)

clientSocket.close()

