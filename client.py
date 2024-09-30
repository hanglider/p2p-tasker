import requests

def send_message(server_ip, message):
    url = f'http://{server_ip}:5000/message'
    data = {'message': message}
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"Ответ от сервера: {response.json()['response']}")
        else:
            print(f"Ошибка сервера: {response.status_code}")
    except Exception as e:
        print(f"Ошибка подключения: {e}")

if __name__ == '__main__':
    server_ip = input("Введите IP сервера: ")  # IP-адрес сервера
    while True:
        message = input("Введите сообщение (или 'exit' для выхода): ")
        if message.lower() == 'exit':
            break
        send_message(server_ip, message)
