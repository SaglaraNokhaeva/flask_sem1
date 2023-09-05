# Задание №9
# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index2.html')


@app.route('/clothing/')
def clothing():  # put application's code here
    return render_template('clothing.html')


@app.route('/shoes/')
def shoes():  # put application's code here
    return render_template('shoes.html')

@app.route('/jackets/')
def jackets():  # put application's code here
    return render_template('jackets.html')


if __name__ == '__main__':
    app.run()
