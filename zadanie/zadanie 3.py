#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    summ = 1
    while True:
        message = int(input("Введите число: "))
        summ *= message
        if summ == 0:
            print('Произведение равно 0')
            break
        else:
            print(f'Полчившееся прозведение: {summ}')


if __name__ == '__main__':
    main()
