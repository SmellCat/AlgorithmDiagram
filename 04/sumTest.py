# -*- coding:utf-8 -*-

__author__ = "Atituset"

import copy


def sumTest(ls):
    ls = copy.copy(ls)
    if len(ls) == 0:
        return 0
    if len(ls) == 1:
        return ls[0]
    else:
        return ls.pop(0) + sumTest(ls)


if __name__ == '__main__':
    a = []
    print(sumTest(a))
    b = [1]
    print(sumTest(b))
    c = [1, 2]
    print(sumTest(c))
    d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sumTest(d))
    print(sum(d))