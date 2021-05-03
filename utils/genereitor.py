import random


class Genereitor:
    def genereitor_password(letter, number, number_caracter):
        try:
            o = str(letter + "," + number)
            f = o.split(',')
            randon = random.choices(f, k=number_caracter)
            return "".join(randon)
        except Error as e:
            print(e)
            return e
        