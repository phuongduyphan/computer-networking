from socket import *

serverPort = 12000

# IPv4, UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)
# bind the port number to the socket
serverSocket.bind(('127.0.0.1', serverPort))

print 'The Server is ready to receive'

while 1:
	# receive message and address from the client
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.upper()
    # send the modified message to the client
    serverSocket.sendto(modifiedMessage, clientAddress)

