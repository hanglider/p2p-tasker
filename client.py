import requests

def send_message(server_ip, index):
    url = f'http://{server_ip}:5000/message'
    data = {'message': message}
    crop = {'crop1' : {0:500, 0:500},
            'crop2' : {500:1000, 500:1000}
    }
    data = crop[f'crop{index}']
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"Ответ от сервера: {response.json()['response']}")
        else:
            print(f"Ошибка сервера: {response.status_code}")
    except Exception as e:
        print(f"Ошибка подключения: {e}")

if __name__ == '__main__':
    server_ip1 = input("Введите IP сервера1: ")
    server_ip2 = input("Введите IP сервера2: ")
    server = 0
    while server == 0:
        message = input("Введите сообщение (или 'exit' для выхода): ")
        if message.lower() == 'exit':
            server = 1
        send_message(server_ip1, message)
    while server == 1:
        message = input("Введите сообщение (или 'exit' для выхода): ")
        if message.lower() == 'exit':
            break
        send_message(server_ip2, message)
