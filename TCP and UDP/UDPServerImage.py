from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', serverPort))

print 'The Server is ready to receive'

# create a image file. Image file will have name 'picture-receive-udp.jpg' at
# the same folder of the python scripts file
file = open('picture-receive-udp.jpg', 'wb+');
while 1:
    bytesToReceive, clientAddress = serverSocket.recvfrom(20000)
    serverSocket.sendto('Packet received', clientAddress)
    # each time the server receive a packet, it writes the data of each 
    # packet to image file
    file.write(bytesToReceive)