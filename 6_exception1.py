"""

Домашнее задание №1

Исключения: KeyboardInterrupt

*   Перепишите функцию hello_user() из задания while1, чтобы она 
    перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
    и завершала работу при помощи оператора break
    
"""

def hello_user():
    
    the_answer = input('How are you?  ')
    while the_answer.lower() not in ['good', 'fine', 'nice']:
        try:
            the_answer = input('How are you?  ')
        except KeyboardInterrupt:
            break
    
if __name__ == "__main__":
    hello_user()
