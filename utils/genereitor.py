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



        