from flask import Flask, render_template, request, redirect, session, flash, url_for
import random

class Genereitor:
    def genereitor_password(letter, number, number_caracter):
        try:
            join_arr = str(letter + "," + number)
            tratament = join_arr.split(',')
            randon = random.choices(tratament, k=number_caracter)
            return "".join(randon)
        except Error as e:
            print(e)
            return e

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
    return redirect(url_for('result'))

@app.route("/result")
def result():
    return render_template('result.html')




if __name__ == '__main__':
    app.run(debug=True)