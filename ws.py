# This program implements a basic webserver.
import socket

print('Webserver starting')

with socket.socket() as s:
  s.bind( ('0.0.0.0', 14000) )
  s.listen()
  conn,addr = s.accept()
  with conn:
    print('Incoming connection from:', addr)
    # receive the incoming request
    request = conn.recv(2048)
    print('REQUEST:', request.decode())

print('Webserver complete')
