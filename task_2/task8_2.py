

'''
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать 
скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), 
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря 
в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра. 
'''
import json

def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json') as f_n:
        dict_to_json = json.load(f_n)
        print(dict_to_json)
        dict_to_json['orders'].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        })
    with open('orders.json', 'w') as f_n:
        json.dump(dict_to_json, f_w, indent=4)


if __name__ == "__main__":
    write_order_to_json('принтер', 10, 6700, 'Ivanov I.I.', '24.09.2017')
    write_order_to_json('scaner', 20, 10000, 'Petrov P.P.', '11.01.2018')
    write_order_to_json('scaner', 20, 10000, 'Petrov P.P.', '11.01.2018')
    write_order_to_json('scaner', 20, 10000, 'Petrov P.P.', '11.01.2018')