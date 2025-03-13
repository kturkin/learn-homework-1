"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    input_list = [
                {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
                {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
                {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
                ]
    
    for data_line in input_list:
        the_sum = sum(data_line['items_sold'])
        product = data_line['product']
        print(f'{product} total: {the_sum}')

        the_avg = avg(data_line['items_sold'])
        print(f'{product} average: {the_avg}')


    total_sells_list = merge_sells_data(input_list)

    total_sells_sum = sum(total_sells_list)
    print (f'Total sells for all products: {total_sells_sum}')

    total_sells_average = avg(total_sells_list)
    print (f'Average sells for all products: {total_sells_average}')


def avg(dataList):
    return sum(dataList) / len(dataList)


def merge_sells_data(input_list):
    
    compound_list = []
    for data_line in input_list:
        compound_list.extend(data_line['items_sold'])
    
    return compound_list
        
if __name__ == "__main__":
    main()
