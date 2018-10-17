from socket import *
serverPort = 12000

#IPv4, TCP
serverSocket = socket(AF_INET,SOCK_STREAM)

# serverSocket will be the welcoming socket
serverSocket.bind(('127.0.0.1',serverPort))

# maximum number of queued connections is at least 1
serverSocket.listen(1)

print 'The server is ready to receive'
while 1:
	# create new socket in the server dedicated to the particular client
    connectionSocket, addr = serverSocket.accept()
    # receive sentence from the client
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    # send modified sentences to the client
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
