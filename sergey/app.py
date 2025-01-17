from flask import Flask, render_template  # из фласка импортируем класс(Flask), подключаем (рендрим) шаблоны из фласка

app = Flask(__name__)  # делаем экземпляр класса

@app.route("/")  # c помощью декоратора @app делаем зрительный образ, то что должно показывать на главной странице
def index():  # сопоставляем конкретный роутинг конкретной функции
    user_name = 'Сергей'
    return render_template('index.html', user_name=user_name)  # возвращаем в главной функции результат выполнения функции рендер_темплэйт

@app.route("/test")  # c помощью декоратора @app делаем зрительный образ, то что должно показывать странице
def test():
    return render_template('test.html')