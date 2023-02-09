# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X


from random import randint
try:
    n = int(input('Введите размер массива: '))

    array = [randint(1, 10) for i in range(n)]
    print('Ваш массив:', array)

    x = int(input('Введите интересующее вас число: '))

    min = abs(x - array[0])
    result = array[0]

    for i in range(1, len(array)):
        if min > abs(array[i] - x):
            min = abs(array[i] - x)
            result = array[i]
    print(f'Самый близкий к заданному числу элемент массива со значением: {result}')
except:
    print('Вы ввели неверные данные!')
