"""
Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def even_odd(number, var_even, var_odd):
    if number == 0:
        return var_even, var_odd
    else:
        temp = number % 10
        number = number // 10
        if temp % 2 == 0:
            return even_odd(number, var_even + 1, var_odd)
        elif temp % 2 == 1:
            return even_odd(number, var_even, var_odd + 1)


class NewEx(Exception):
    pass


try:
    number = int(input("Введите натуральное число: "))
    if number < 0:
        raise NewEx
    print(
        f"Количество четных и нечетных цифр в числе равно: {even_odd(number, 0, 0)}")
except ValueError:
    print("Введите натуральное число")
except NewEx:
    print('Работаем с натуральными числами')
