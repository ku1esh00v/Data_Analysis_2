#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import jsonschema
from jsonschema import validate


def save_data(filename):
    with open(filename, 'w') as file:
        json.dump(trains, file, indent=4)
    print(f'Данные сохранены в файл {filename}')

def load_data(filename):
    global trains
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            # Проверка на валидность загруженных данных
            for item in data:
                validate(instance=item, schema=train_schema)
            trains = data
            print(f'Данные успешно загружены из файла {filename}')
    except Exception as e:
        print(f'Ошибка загрузки данных из файла: {e}', file=sys.stderr)


# JSON схема для данных о поездах
train_schema = {
    "type": "object",
    "properties": {
        "destination": {"type": "string", "pattern": "^[A-Za-z ]+$"},
        "number": {"type": "string", "pattern": "^[0-9]+$"},
        "departure_time": {"type": "string", "pattern": "^([01]?[0-9]|2[0-3]):[0-5][0-9]$"}
    },
    "required": ["destination", "number", "departure_time"]
}


if __name__ == '__main__':
    trains =[]
    # Организация бесконечного цикла запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input('>>> ').lower()

        # Выполнить действие в соответствии с командой.
        if command == 'exit':
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

            # Валидация данных с использованием JSON Schema.
            try:
                jsonschema.validate(train, train_schema)
            except jsonschema.exceptions.ValidationError as e:
                print(f'Ошибка валидации данных: {e}')
                continue

            # Добавить словарь в список.
            trains.append(train)

            # Отсортировать список по времени отправления поезда.
            trains.sort(key=lambda item: item.get('departure_time', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+{}-+{}-+'.format(
                '-' * 20,
                '-' * 15,
                '-' * 20
            )
            print(line)
            print(
                '| {:^20} | {:^15} | {:^20} |'.format(
                    "Пункт назначения",
                    "Номер поезда",
                    "Время отправления"
                )
            )
            print(line)

            # Вывести информацию о поездах.
            for idx, train in enumerate(trains, 1):
                print(
                    '| {:<20} | {:^15} | {:^20} |'.format(
                        train.get('destination', ''),
                        train.get('number', ''),
                        train.get('departure_time', '')
                    )
                )
            print(line)

        elif command.startswith('select '):
            # Получить название пункта назначения из команды.
            parts = command.split(' ', maxsplit=1)
            destination = parts[1]

            # Поиск поездов с заданным пунктом назначения.
            selected_trains = [train for train in trains if train['destination'] == destination]

            if selected_trains:
                # Вывести информацию о найденных поездах в виде таблицы.
                line = '+-{}-+{}-+{}-+'.format(
                    '-' * 20,
                    '-' * 15,
                    '-' * 20
                )
                print(line)
                print(
                    '| {:^20} | {:^15} | {:^20} |'.format(
                        "Пункт назначения",
                        "Номер поезда",
                        "Время отправления"
                    )
                )
                print(line)
                for train in selected_trains:
                    print(
                        '| {:<20} | {:^15} | {:^20} |'.format(
                            train.get('destination', ''),
                            train.get('number', ''),
                            train.get('departure_time', '')
                        )
                    )
                print(line)
            else:
                print(f'Поездов в пункт "{destination}" не найдено')


        elif command == 'help':
            # Вывести справку о работе с программой.
            print('Список команд:\n')
            print('add - добавить информацию о поезде;')
            print('list - вывести список всех поездов;')
            print('select <пункт_назначения> - запросить информацию о поездах в заданном пункте назначения;')
            print('exit - завершить работу с программой.')
        elif command.startswith('save'):
            filename = command.split(' ')[1]
            save_data(filename)

        elif command.startswith('load'):
            filename = command.split(' ')[1]
            load_data(filename)
        else:
            print(f'Неизвестная команда "{command}"!', file=sys.stderr)




