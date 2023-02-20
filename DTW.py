#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *


def get_difference(s1, s2):

    r, c = len(s1), len(s2)

    d1 = zeros((r, c))

    for i in range(len(s2)):
        if i == 0:
            d1[0][i] = abs(s2[i] - s1[0])
        else:
            d1[0][i] = abs(s2[i] - s1[0]) + d1[0][i - 1]

    for j in range(len(s1)):
        if j == 0:
            d1[j][0] = abs(s1[j] - s2[0])
        else:
            d1[j][0] = abs(s1[j] - s2[0]) + d1[j - 1][0]

    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            d1[i][j] = abs(s1[i] - s2[j]) + min(d1[i - 1][j - 1],
                                                d1[i - 1][j],
                                                d1[i][j - 1])
    i, j = array(d1.shape) - 1

    path = [(i, j)]

    while i > 0 or j > 0:
        min_index = argmin((d1[i - 1][j - 1], d1[i][j - 1], d1[i - 1][j]))
        if min_index == 0:
            i -= 1
            j -= 1
        elif min_index == 1:
            j -= 1
        else:
            i -= 1
        path.insert(0, (i, j))

    # print(d1[-1, -1] / sum(d1.shape))
    # print(path)
    # print(d1)

    return d1[-1, -1] / sum(d1.shape)



