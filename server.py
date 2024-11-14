import socket
import threading

def handle_client(client_socket, client_address):
    print(f'Conexión desde: {client_address}')
    
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            
            message = data.decode().strip()
            print(f'Mensaje recibido de {client_address}: {message}')
            
            if message == 'DESCONEXION':
                print(f'Cerrando conexión con {client_address}...')
                break
            else:
                response = message.upper().encode()
                client_socket.sendall(response)
    
    finally:
        client_socket.close()
        print(f'Conexión cerrada con {client_address}')

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(5) 
    print('Servidor TCP iniciado y escuchando en el puerto 5000...')
    
    while True:
        print('Esperando conexión de un cliente...')
        client_socket, client_address = server_socket.accept()
        
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == '__main__':
    main()
