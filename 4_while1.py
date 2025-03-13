"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    
    the_answer = input('How are you?  ')
    while the_answer.lower() not in ['good', 'fine', 'nice']:
        the_answer = input('How are you?  ')


if __name__ == "__main__":
    hello_user()
