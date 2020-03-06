# coding=utf-8
dec = [3000, 2000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100,
       90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
rome = ['MMM', 'MM', 'M', 'CM', 'DCCC', 'DCC', 'DC', 'D', 'CD', 'CCC', 'CC', 'C',
        'XC', 'LXXX', 'LXX', 'LX', 'L', 'XL', 'XXX', 'XX', 'X', 'IX', 'VIII', 'VII', 'VI', 'V', 'IV', 'III', 'II', 'I']


def dec_to_rome(number: object) -> object: #Переводим десятичное число в римское
    i = 0
    out = ''
    rm = ''
    for symb in str(number): # Разбираем десятичное число на тысячи, сотни, десятки единицы
        i += 1  #
        num_degr = 10 ** (len(str(number)) - i)
        exp = int(symb) * num_degr
        try:                # Ищем в списке rome значения с индексом соответствующим индексу списка dec
            rm += rome[dec.index(exp)]
        except:
            rm += ''  # Если значение не найдено, то в итоговую переменную rm добавляем пустое значение

    return rm


def rome_to_dec(rome_val):  # Переводим римское число в десятичное
    dc = 0
    for decimal, roman in zip(dec, rome): # Перебираем одновременно два списка
        while rome_val.startswith(roman): # Ищем совпадения в списке rome с уменьшением строки rome_val при последующей итерации
            dc += decimal
            rome_val = rome_val[len(roman):]

    return dc


def roman_sum(first_number: str, second_number: str) -> str: # Суммируем римские числа
    sum_rom = dec_to_rome(rome_to_dec(first_number)+rome_to_dec(second_number))
    print(first_number, " + ", second_number," = ", sum_rom)


num1 = int(input("Введите первое десятичное число: "))
num2 = int(input("Введите второе десятичное число: "))

num12 = num1 + num2
print(num1, ' + ', num2,' = ',num12)

num1 = dec_to_rome(num1)
num2 = dec_to_rome(num2)
roman_sum(num1, num2)
