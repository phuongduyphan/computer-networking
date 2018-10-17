from PIL import Image
from socket import *
import io

# convert the image to binary data
image = Image.open('music.jpg')
imgBinary = io.BytesIO()
image.save(imgBinary, format='JPEG')
imgBinary = imgBinary.getvalue()

# send binary data of the image through TCP
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
clientSocket.send(imgBinary)
message = clientSocket.recv(1024)
print 'From Server:', message
clientSocket.close()

