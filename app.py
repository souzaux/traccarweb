#!/usr/bin/python
from flask import Flask, render_template
from flask import redirect, url_for, request, jsonify
import requests

app = Flask(__name__)

def login(login_data):
    s = requests.session()
    s.post(baseUrl + '/session', data=login_data)
    return s


@app.route('/healthcheck')
def healthcheck():
    return jsonify({'VERSION': '0.1.1', 'STATUS': 'WORKING'})


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        login_data = dict(email=email, password=password)
        coockie = login(login_data)
        if coockie.status_code != 200:
            error = 'Invalid credentials. Please try again.'
        else:
            return redirect(url_for('home', coockie))
    return render_template('login.html', error=error)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return 'Bye Bye!'


# consumir um recurso da api:
@app.route('/devices', methods=['GET', 'POST'])
def devices():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
