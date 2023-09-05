# Задание №8
# Создать базовый шаблон для всего сайта, содержащий
# общие элементы дизайна (шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты",
# используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/about/')
def about():  # put application's code here
    return render_template('about.html')


@app.route('/contact/')
def contact():  # put application's code here
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
