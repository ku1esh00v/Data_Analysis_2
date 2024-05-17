#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

# Путь к файлу для сохранения данных о поездах.
file_path = 'data/trains.json'

def save_data(data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def load_data():
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

if __name__ == '__main__':
    # Загрузить данные из файла при запуске программы.
    trains = load_data()

    # Организация бесконечного цикла запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input('>>> ').lower()

        # Выполнить действие в соответствии с командой.
        if command == 'exit':
            # Сохранить данные перед выходом.
            save_data(trains)
            break
        elif command == 'add':
            # Запросить данные о поезде.
            destination = input('Название пункта назначения? ')
            number = input('Номер поезда? ')
            departure_time = input('Время отправления? ')

            # Создать словарь.
            train = {
                'destination': destination,
                'number': number,
                'departure_time': departure_time
            }

            # Добавить словарь в список.
            trains.append(train)

            # Отсортировать список по времени отправления поезда.
            trains.sort(key=lambda item: item.get('departure_time', ''))

        elif command == 'list':
            # Вывести информацию о поездах.
            for idx, train in enumerate(trains, 1):
                print(f'{idx}. Пункт назначения: {train["destination"]}, Номер поезда: {train["number"]}, Время отправления: {train["departure_time"]}')

        # Другие команды остаются без изменений.

        elif command == 'help':
            # Вывести справку о работе с программой.
            print('Список команд:\n')
            print('add - добавить информацию о поезде;')
            print('list - вывести список всех поездов;')
            print('select <пункт_назначения> - запросить информацию о поездах в заданном пункте назначения;')
            print('exit - завершить работу с программой.')
        else:
            print(f'Неизвестная команда "{command}"!', file=sys.stderr)
            
