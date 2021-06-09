from flask import Flask, render_template, request, redirect, session, flash, url_for
from utils.genereitor import Genereitor

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/genereitor', methods=['POST', ])
def genereitor():
    latter = request. form['latter']
    number = request. form['number']
    number_caracter = request. form['number_caracter']
    result = Genereitor.genereitor_password(latter, str(number), int(number_caracter))
    return result


if __name__ == '__main__':
    app.run(debug=True)