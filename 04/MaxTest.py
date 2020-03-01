# -*- coding:utf-8 -*-

__author__ = "Atituset"


def MaxTest(ls):
    maxVal = ls[0]
    for item in ls[1:]:
        if item > maxVal:
            maxVal = item
    return maxVal


if __name__ == '__main__':
    a = [1, 2, 3]
    print(MaxTest(a))