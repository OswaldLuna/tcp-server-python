import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(('localhost', 5000))
    print("Conectado al servidor en el puerto 5000.")

    while True:
        message = input('Ingresa un mensaje (o "DESCONEXION" para salir): ')
        client_socket.sendall(message.encode())
        
        if message == 'DESCONEXION':
            print('Cerrando conexión con el servidor...')
            break
        
        response = client_socket.recv(1024)
        if not response:
            print("El servidor cerró la conexión.")
            break

        print('Respuesta del servidor:', response.decode())

except ConnectionRefusedError:
    print("No se pudo conectar al servidor. Asegúrate de que el servidor esté ejecutándose.")
except socket.error as e:
    print(f"Error de conexión: {e}")
finally:
    client_socket.close()
