# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input('Введите день недели: '))
if number < 1 or number > 7:
    print('День в не диапазона недели')
elif number == 6 or number == 7:
    print('Этот день выходной')
else:
    print('Этот день рабочий')