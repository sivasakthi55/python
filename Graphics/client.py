import socket
s=socket.socket()
host=socket.gethostname()
port=12346

s.connect((host,port))
a=s.recv(1024)
print(a.decode()+" i am a client one")
s.close()

                        