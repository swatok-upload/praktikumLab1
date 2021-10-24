import socket

klient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
klient.connect(('localhost', 9090)) #конектимся к ip адресу сервера по порту

while True:
    print('вы в клиенте')

    klient.send(input('введите письмо').encode("utf-8")) #отправляем письмо на сервер
    data = klient.recv(1024)  # получаем кол-во информации за 1 пакет в размере 1024 байта

    break
klient.close() #закрываем соединение

print(data.decode("utf-8"))  # полученная информация