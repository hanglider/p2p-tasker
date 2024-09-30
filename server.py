from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def receive_message():
    data = request.json  # Получаем данные из POST-запроса
    print(f"Получено сообщение: {data['message']}")
    return jsonify({'response': 'Сообщение получено!'}), 200  # Возвращаем ответ клиенту

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Сервер доступен по любому IP на порту 5000
