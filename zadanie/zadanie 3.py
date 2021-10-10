#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    composition = 1
    while True:
        message = int(input("Введите число: "))
        composition *= message
        if composition == 0:
            print('Произведение равно 0')
            break
        else:
            print(f'Полчившееся прозведение: {composition}')


if __name__ == '__main__':
    main()
