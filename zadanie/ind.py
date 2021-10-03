#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def select(line, flot):
    nom = input('Введите тип желаемого самолёта: ')
    count = 0
    print(line)
    print(
        '| {:^4} | {:^20} | {:^15} | {:^16} |'.format(
            "№",
            "Место прибытия",
            "Номер самолёта",
            "Тип"))
    print(line)
    for i, num in enumerate(flot, 1):
        if nom == num.get('value', ''):
            count += 1
            print(
                '| {:<4} | {:<20} | {:<15} | {:<16} |'.format(
                    count,
                    num.get('stay', ''),
                    num.get('number', ''),
                    num.get('value', 0)))
    print(line)
    if count == 0:
        print('Таких рейсов нет')


def table(line, flot):
    print(line)
    print(
        '| {:^4} | {:^20} | {:^15} | {:^16} |'.format(
            "№",
            "Место прибытия",
            "Номер самолёта",
            "Тип"))
    print(line)
    for idx, worker in enumerate(flot, 1):
        print(
            '| {:<4} | {:<20} | {:<15} | {:<16} |'.format(
                idx,
                worker.get('stay', ''),
                worker.get('number', ''),
                worker.get('value', 0)
            )
        )
    print(line)


def add(flot):
    value = input('Введите тип самолёта: ')
    number = input('Введите номер самолёта: ')
    stay = input('Введите место прибытия: ')
    air = {
        'number': number,
        'stay': stay,
        'value': value
    }
    flot.append(air)
    if len(flot) > 1:
        flot.sort(key=lambda x: x.get('stay', ''))


def main():
    flot = []
    print('Список комманд: \n exit - Завершить работу \n add - Добавить рейс \n'
          ' list - Показать список рейсов \n select - Выбрать рейсы по типу самолёте')
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 20,
        '-' * 15,
        '-' * 16
    )
    while True:
        com = input('Введите команду: ').lower()
        if com == 'exit':
            break
        elif com == "add":
            add(flot)
        elif com == 'list':
            table(line, flot)
        elif com == 'select':
            select(line, flot)
        else:
            print(f"Неизвестная команда {com}", file=sys.stderr)


if __name__ == '__main__':
    main()
