import socket
import time

host_name = 'localhost'
port = 5655

sc = socket.socket()
sc.bind((host_name,port))
sc.listen(5)    
connect, addres  = sc.accept()

print(str(addres) + 'Conncented server ')

while True:
    while True:
        try:
             getdata =  str(connect.recv(1024).decode())
             print('Clint:'+ getdata)
             break
        except ConnectionResetError:
            time.sleep(2)
            connect, addres  = sc.accept()
            print(str(addres)+' İs Come ')
    if getdata == '12exit':
        break
    else:
        msg = input('--:')
        print('geliyo')
        connect.send(msg.encode())
connect.close()
