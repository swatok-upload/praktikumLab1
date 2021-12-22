#увеличили кол-во клиентов, которые могут подключиться до двух. Клиент можно использовать от Эхо сервера. В итоге, он подключает все клиенты, и только когда все напишут 
#сообщение, он всем отправит их сообщение.
import socket  

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind(('localhost', 9090))  

sock.listen(2)  

while True:
    print('вы в сервере')
    while True:
        student, address = sock.accept()  
        data = student.recv(1024)
        student.send(data)  
        data = student.recv(1024)  

    print(data.decode("utf-8")) 
