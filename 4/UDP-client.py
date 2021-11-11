import socket


msgromClient = "Hello UDP Server"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("81.12.114.148", 20002)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
print("Message from Server {}".format(msgFromServer[0]))

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
print("Message from Server {}".format(msgFromServer[0]))

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
print("Message from Server {}".format(msgFromServer[0]))
