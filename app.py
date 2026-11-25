from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, PaaS! Лабораторная работа №2. Автоматическое обновление работает!"

if __name__ == "__main__":
    app.run()