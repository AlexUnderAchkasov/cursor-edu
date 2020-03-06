# coding=utf-8
dec = [3000, 2000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100,
       90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
rome = ['MMM', 'MM', 'M', 'CM', 'DCCC', 'DCC', 'DC', 'D', 'CD', 'CCC', 'CC', 'C',
        'XC', 'LXXX', 'LXX', 'LX', 'L', 'XL', 'XXX', 'XX', 'X', 'IX', 'VIII', 'VII', 'VI', 'V', 'IV', 'III', 'II', 'I']


def dec_to_rome(number: object) -> object:
    i = 0
    out = ''
    rm = ''
    for symb in str(number):
        i += 1
        num_degr = 10 ** (len(str(number)) - i)
        exp = int(symb) * num_degr
        try:
            rm += rome[dec.index(exp)]
        except:
            rm += ''

    return rm


def rome_to_dec(rome_val):
    dc = 0
    for decimal, roman in zip(dec, rome):
        while rome_val.startswith(roman):
            dc += decimal
            rome_val = rome_val[len(roman):]

    return dc


num1 = int(input("Введите первое десятичное число: "))
num2 = int(input("Введите второе десятичное число: "))
num12 = num1 + num2
print(num1, ' + ', num2,' = ',num12)

num1 = dec_to_rome(num1)
num2 = dec_to_rome(num2)
num12 = dec_to_rome(num12)

print(num1, " + ", num2, " = ", num12)

