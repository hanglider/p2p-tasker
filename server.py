import socket

def start_server(host='192.168.56.1', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Повторное использование порта
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер запущен на {host}:{port}, ожидает подключения клиентов...")

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Клиент подключился: {client_address}")
            
            while True:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                print(f"Получено сообщение от {client_address}: {data}")
                client_socket.send(f"Сообщение '{data}' получено".encode('utf-8'))
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            client_socket.close()
            print(f"Клиент {client_address} отключился.")

if __name__ == "__main__":
    start_server()
