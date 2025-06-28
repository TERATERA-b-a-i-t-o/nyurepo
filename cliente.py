import socket


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("El nombre de su computadora es: " + hostname)
print("La dirección IP de su computadora es: " + ip)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
client_socket.connect((ip, 12345)) 


respuesta = client_socket.recv(1024).decode()
print(respuesta)


pregunta = client_socket.recv(1024).decode()
ansuwa = input(pregunta + " ")


client_socket.send(ansuwa.encode())

mensaje_00 = client_socket.recv(1024).decode()
print(mensaje_00)


client_socket.close()