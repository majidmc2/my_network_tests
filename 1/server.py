import socket
import time

s = socket.socket()
s.bind(("localhost", 5000))
s.listen(10)
c, a = s.accept()

print("Receiving....")
while True:
   data = c.recv(20)
   print(str(data))
   time.sleep(5)
   print("Sleep for 5 second but data bufferd!")

c.close()
s.close()
