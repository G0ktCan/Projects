import socket
import time

host_name = 'localhost'
port = 5655

sc = socket.socket()
sc.bind((host_name,port))
sc.listen(5)
connect, addres  = sc.accept()
msg = input(':--')
print('Conncentied  sucsesfull {}:{}'.format(host_name,port))

while msg != '12exit':
    sc.send(msg.encode())
    gd = sc.recv(1024).decode()
    
    print('Server-'+gd)
    msg = input(':--')
sc.close()