#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def test():
    message = int(input('Введите целое число:'))
    if message > 0:
        positive(message)
    else:
        negative(message)


def negative(message):
    print(f'Число {message} отрицательное')


def positive(message):
    print(f"Число {message} положительное")


if __name__ == '__main__':
    test()
