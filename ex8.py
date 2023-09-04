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
    return render_template('index.html', name = 'index')


@app.route('/about/')
def about():  # put application's code here
    return render_template('about.html', name = 'about')


@app.route('/contacts/')
def contacts():  # put application's code here
    return render_template('contacts.html', name = 'contacts')


@app.route('/add-nums/<int:num>/<int:num2>')
def add_nums(num, num2):


    return str(num + num2)


@app.route('/str-len/<str_inp>')
def str_len(str_inp):


    return str(len(str_inp))


@app.route('/students/')
def students():


    _students = [
        {
            "name": "John",
            "surname": "Doe",
            "age": 20,
            "average": 85
        },
        {
            "name": "Jane",
            "surname": "Smith",
            "age": 22,
            "average": 92
        },
    ]
    context = {'students': _students}
    return render_template('students.html', **context)


@app.route('/news/')
def news():


    _news = [
        {
            "title": "John1",
            "descr": "Doe",
            "date": 201
        },
        {
            "title": "John2",
            "descr": "Doe",
            "date": 202
        },
        {
            "title": "John3",
            "descr": "Doe",
            "date": 203
        },
    ]
    context = {'news': _news}
    return render_template('news.html', **context)

if __name__ == '__main__':
    app.run()
