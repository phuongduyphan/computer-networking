# the socket module forms the basis of all network communications in Python
from socket import *

# the host is localhost
serverName = '127.0.0.1'
serverPort = 12000

#IPv4, UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = raw_input('Input lowercase sentence:')
# send the message to the server
clientSocket.sendto(message, (serverName, serverPort))
# receive the message from the server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()

