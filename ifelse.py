"""
Dado un número entero,, realice las siguientes acciones condicionales:

Sies impar, imprimirWeird
Sies par y en el rango inclusivo dea, impresiónNot Weird
Sies par y en el rango inclusivo dea, impresiónWeird
Sies par y mayor que, impresiónNot Weird
"""


def is_even(n):
    if n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <=5:
        print("Not Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
    elif n % 2 == 1:
        print("Weird")




if __name__ == '__main__':
    is_even(int(input()))

