import time, sys, socket

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080

new_socket.bind((host_name, port))
print("Привязка выполнена успешно!")
print("Это ваш Ip: ", s_ip)

name = input("Введите ваш никнайм: ")
new_socket.listen(1)

conn, add= new_socket.accept()
print("Получено соединение от ", add[0])
print("Соединение установлено. Подключено из: ", add[0])

client = (conn.recv(1024)).decode()
print(client + "Подключение установленно.")

conn.send(name.encode())
while True:
    message = input("Я: ")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)