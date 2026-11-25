
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, PaaS! Лабораторная работа №2. Студент: Ляльков"

if __name__ == "__main__":
    app.run()
