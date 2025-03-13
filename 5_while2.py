"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {'How are you?' : 'All good',
                         'What do you do?' : "I'm working",
                         "What's new?" : 'Started learning python'}

def ask_user(answers_dict: dict):

    the_question = input('Talk to me: ')

    while the_question.lower() not in ['bye', 'stop', 'exit', 'finish']:
        
        the_answer = answers_dict.get(the_question, 'Ask something else')
        print(the_answer)
        the_question = input('Talk to me: ')
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
