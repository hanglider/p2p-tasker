import socket

def start_client(server_ip, server_port=8080):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        print(f"Подключен к серверу {server_ip}:{server_port}")

        while True:
            message = input("Введите сообщение (или 'exit' для выхода): ")
            if message.lower() == 'exit':
                break
            client_socket.send(message.encode('utf-8'))

            response = client_socket.recv(1024).decode('utf-8')
            print(f"Ответ от сервера: {response}")
    except Exception as e:
        print(f"Ошибка подключения: {e}")
    finally:
        client_socket.close()
        print("Отключено от сервера.")

if __name__ == "__main__":
    server_ip = input("Введите IP сервера: ")
    start_client(server_ip)
