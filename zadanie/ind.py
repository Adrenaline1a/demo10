#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


if __name__ == '__main__':
    flot = []
    print('Список комманд: \n exit \n add \n list \n select')
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
            tip = input('Введите тип самолёта: ')
            nomer = input('Введите номер самолёта: ')
            mesto = input('Введите место прибытия: ')
            aflot = {
                'nomer': nomer,
                'mesto': mesto,
                'tip': tip
            }
            flot.append(aflot)
            if len(flot) > 1:
                flot.sort(key=lambda x: x.get('mesto', ''))
        elif com == 'list':
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
                        worker.get('mesto', ''),
                        worker.get('nomer', ''),
                        worker.get('tip', 0)
                    )
                )
            print(line)
        elif com == 'select':
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
                if nom == num.get('tip', ''):
                    count += 1
                    print(
                        '| {:<4} | {:<20} | {:<15} | {:<16} |'.format(
                        count,
                        num.get('mesto', ''),
                        num.get('nomer', ''),
                        num.get('tip', 0)))
            print(line)
            if count == 0:
                print('Таких рейсов нет')
        else:
            print(f"Неизвестная команда", file=sys.stderr)