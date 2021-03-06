from socket import socket, AF_INET, SOCK_STREAM
from ssl import SSLContext, PROTOCOL_TLS_SERVER


ip = '127.0.0.1'
port = 8443
context = SSLContext(PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert.pem', 'key.pem')

with socket(AF_INET, SOCK_STREAM) as server:
    server.bind((ip, port))
    server.listen(5)
    with context.wrap_socket(server, server_side=True) as tls:
        connection, address = tls.accept()
        print(f'Connected by {address}')
        connection.sendall(b"You're welcome\n")
        data = connection.recv(1024)
        print(f'Client: {data}')

        
