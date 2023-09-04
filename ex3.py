# Задание №3
# Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world(): # put application's code here
    return 'Hello World!'

@app.route('/add-nums/<int:num>/<int:num2>')
def add_nums(num, num2):
    return str(num+num2)

if __name__ == '__main__':
    app.run()