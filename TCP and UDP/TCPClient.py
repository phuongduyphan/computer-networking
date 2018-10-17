from socket import *

serverName = '127.0.0.1' 
serverPort = 12000

# IPv4, TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# initiate the TCP connection between the client and server; three-way
# handshake is performed and a TCP connection is established between 
# the client and the server
clientSocket.connect((serverName,serverPort))

sentence = raw_input('Input lowercase sentence:')

# send the sentence through client 's socket and into the TCP connection
clientSocket.send(sentence)

# receive the modified sentence from the server
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence

clientSocket.close()
