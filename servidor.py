#realizar un programa cliente servidor donde el cliente debe enviarle al servidor un nombre de usuario al inicio de la conexion.
#El servidor debe ser concurrente, pedirle al cliente el nombre de usuario. Este nombre de usuario que recibe lo debe usar para
#enviarle la api que consultara en la pokkeapi cuando el cliente le envie el comando /eso.
#El programa debe terminar cuando el cliente le envie /adios al servidor, el cual antes de terminar la conexion debe enviar un saludo
#la evaluacion se debe enviar via una invitacion de git a donde esta subido el codigo "javierblanco.edu"

import socket
import requests

url = 'https://pokeapi.co/api/v2/version/3/'

pasu = {"iusa" : "ses"}


hostname = socket.gethostname() 
ip = socket.gethostbyname(hostname) 
print("El nombre de su computadora es: " + hostname)
print("La dirección IP de su computadora es: " + ip)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server_socket.bind((ip, 12345)) 
server_socket.listen(1) 

print("server escuchando en el puerto 12345 si quesi")

while True:

    
    client_socket, address = server_socket.accept()
    print("se establecio una conexion con " + str(address) + "yippe :D")

    
    client_socket.send("america ya, saludosss, desde el servidor.".encode())

    pregunta = "Ingrese su usuario:"
    ansuwa = client_socket.recv(1024).decode()
    print("Su usuario: ", ansuwa)

    

    if ansuwa == pasu["usuario"]:
        print("god")
        client_socket.send("te envio cositas juasjuasjuas".encode())
        resp = requests.get(url)
        if resp.status_code == 200:
            pokever = resp.json()
            
            for x in pokever[:3]:
                print(x['names'])
        
    else:
        print("nope.")
        client_socket.send("Cierre de conexion.".encode())
        client_socket.close()


    client_socket.close()
    
    
    