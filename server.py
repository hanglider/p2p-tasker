from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/home")
def home():
    return "глеб красава"

@app.route("/dom")
def dom():
    return "арсений лох ибани"

@app.route('/message', methods=['POST'])
def receive_message():
    data = request.json  # Получаем данные из POST-запроса
    print(f"Получено сообщение: {data['message']}")
    return jsonify({'response': 'Сообщение получено!'})  # Возвращаем ответ клиенту

if __name__ == '__main__':
    app.run(host='172.20.10.2', port=5000)  # Нужно вставить ip роутера
