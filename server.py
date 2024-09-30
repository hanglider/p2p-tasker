import socket

def start_server(host='0.0.0.0', port=12345):
    # Создание TCP сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер запущен на {host}:{port}, ожидает подключения клиентов...")

    while True:
        # Ожидание клиента
        client_socket, client_address = server_socket.accept()
        print(f"Клиент подключился: {client_address}")
        
        # Получение и отправка сообщений
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Получено сообщение от {client_address}: {data}")
            client_socket.send(f"Сообщение '{data}' получено".encode('utf-8'))
        
        client_socket.close()
        print(f"Клиент {client_address} отключился.")

if __name__ == "__main__":
    start_server()
