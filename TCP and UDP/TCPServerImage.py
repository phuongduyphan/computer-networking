from PIL import Image
import io
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
	connectionSocket, addr = serverSocket.accept()
	# receive binary data of images from clients
	imgBinary = connectionSocket.recv(65536);
	# convert binary data to image type
	image = Image.open(io.BytesIO(imgBinary))
	# show image 
	image.show()
	connectionSocket.send('image received')
	connectionSocket.close()
