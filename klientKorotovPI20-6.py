import socket 

klient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
klient.connect(('localhost', 9225)) #конектимся к ip адресу сервера по порту

while True:
    information = klient.recv(1024) #получаем кол-во информации за 1 пакет в размере 1024 байта
    print(information.decode('utf-8')) #полученная информация
    klient.send(input().encode('utf-8')) #отправляем письмо на сервер

