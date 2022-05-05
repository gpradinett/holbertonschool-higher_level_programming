#!/usr/bin/python3
def weight_average(my_list=[]):
    numerador = 0
    denominador = 0
    for i in my_list:
        numerador += i[0] * i[1]
        denominador += i[1]
    return (numerador / denominador)
