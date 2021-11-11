import socket


s = socket.socket()
s.connect(("localhost", 5000))
data = b"BbbbbbbbbbbbbbbbbbbbbbbbbbbbbiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiigDaaaaaaaaaaaaaaaaaaaaaaaaaatttttttttttttttttttaaaaaaaaaaaa"

print("Sending...")
s.send(data)

print("Done Sending.")
print(s.recv(1024))
s.close()