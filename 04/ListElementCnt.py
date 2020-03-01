# -*- coding:utf-8 -*-

__author__ = "Atituset"
import copy


def listElementCnt(ls):
    ls = copy.copy(ls)
    if len(ls) == 0:
        return 0
    elif len(ls) == 1:
        return 1
    else:
        ls.pop()
        return 1 + listElementCnt(ls)


if __name__ == '__main__':
    a = []
    print(listElementCnt(a))
    b = [1]
    print(listElementCnt(b))
    c = [1, 2]
    print(listElementCnt(c))
    d = [0, 1,2,3, 4, 5, 6, 7, 8, 9]
    print(listElementCnt(d))