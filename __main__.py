#!/usr/bin/env python3.7

import sys
from random import randint

order_list: [int] = []


def re_roll(val) -> int:
    while val in order_list:
        val = roll()
    return val


def roll() -> int:
    val = randint(1, int(sys.argv[1])+1)
    if val in order_list:
        val = re_roll(val)
    return val


def start():
    for i in range(1, int(sys.argv[1]) + 1):
        order_list.append(roll())

    assert len(order_list) == int(sys.argv[1])

    print(order_list)


try:
    start()
except Exception as e:
    print('\033[1;31m[ERROR] - '+str(e)+'\033[0m')
