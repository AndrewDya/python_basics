"""
Задание 5.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""


"""
На платформе: Задача №2: Найдите сумму цифр трехзначного числа.
"""
a = int(input("Введите трёхзначное число: "))
if 99 < a < 1000:
    result = int(str(a)[0]) + int(str(a)[1]) + int(str(a)[2])
    print(f"Сумма чисел трёхзначного числа: {result}")
else:
    print("Прочтите условие внимательнее")
