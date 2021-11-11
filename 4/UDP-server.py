import socket
import time


localIP = "81.12.114.148"
localPort = 20002
bufferSize = 1024


# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    UDPServerSocket.sendto(str.encode('-- 1'), address)
    time.sleep(5)
    UDPServerSocket.sendto(str.encode('-- 2'), address)
    time.sleep(5)
    UDPServerSocket.sendto(str.encode('-- 3'), address)
