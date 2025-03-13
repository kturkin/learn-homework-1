"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    print("1, 'test_str' result:")
    res = compare_two_vars(1, 'test_str')
    print(res)

    print("'test_str', 'test_str' result:")
    res = compare_two_vars('test_str', 'test_str')
    print(res)

    print("'Loooooong', 'short' result:")
    res = compare_two_vars('Loooooong', 'short')
    print(res)

    print("'Python', 'learn' result:")
    res = compare_two_vars('Python', 'learn')
    print(res)


def compare_two_vars(var1, var2):
    
    output = []

    for i in range(4):

        if i == 0 and not all(isinstance(x, str) for x in [var1, var2]):
            output.append (0)
        if i == 1 and var1 == var2:
            output.append (1)
        if i == 2 and len(str(var1)) > len(str(var2)):
            output.append (2)
        if i == 3 and var1 != var2 and var2 == 'learn':
            output.append (3)
    
    return output


if __name__ == "__main__":
    main()
