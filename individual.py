#Для своего варианта лабораторной работы 2.8 необходимо дополнительно реализовать
#сохранение и чтение данных из файла формата JSON. Необходимо также проследить за тем,
#чтобы файлы генерируемый этой программой не попадали в репозиторий лабораторной
#работы.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def input_data():
    data = []
    while True:
        shop_name = input("Введите название магазина (или 'стоп' для завершения ввода): ")
        if shop_name == "стоп":
            break
        item_name = input("Введите название товара: ")
        item_price = float(input("Введите стоимость товара в рублях: "))
        data.append({
            "название магазина": shop_name,
            "название товара": item_name,
            "стоимость товара в рублях": item_price
        })
    return data

def sort_data(data):
    sorted_data = sorted(data, key=lambda x: x["название магазина"])
    return sorted_data

def display_shop_items(data, shop_name):
    items = [item for item in data if item["название магазина"] == shop_name]
    if items:
        print(f"\nТовары в магазине {shop_name}:")
        for item in items:
            print(f"Товар: {item['название товара']}, Цена: {item['стоимость товара в рублях']} руб.")
    else:
        print(f"Магазин {shop_name} не найден.")

def save_data_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Данные сохранены в файл {filename}")

def load_data_from_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Файл не найден. Создан новый список данных.")
        return []

if __name__ == "__main__":
    data_filename = "data.json"

    # Загрузка данных из файла (если файл существует)
    data = load_data_from_json(data_filename)

    if not data:
        data = input_data()
        save_data_to_json(data, data_filename)

    sorted_data = sort_data(data)

    print("\nДанные о товарах:")
    for item in sorted_data:
        print(f"Магазин: {item['название магазина']}, Товар: {item['название товара']}, Цена: {item['стоимость товара в рублях']} руб.")

    shop_name_input = input("\nВведите название магазина для вывода информации о товарах: ")
    display_shop_items(sorted_data, shop_name_input)

        
