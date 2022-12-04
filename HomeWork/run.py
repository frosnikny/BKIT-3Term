'''
Для запуска сервиса используем команду командной строки:
flask --app run.py run
'''
from flask import Flask
from fibonacci import fibonacci_numbers

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Returning the Fibonacci numbers!</p>"


@app.route('/num/<int:cnt>')
def get_fibonacci(cnt):
    fib_gen = fibonacci_numbers(cnt)
    res = [i for i in fib_gen]
    return res
