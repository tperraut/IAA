#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt


def pfun(p, r, n):
    """
        Calcul de la concentration de mesure
    """
    return (p ** r) * ((1 - p) ** (n - r))


def bibi(r, n):
    """
        Calcul coefficient binomial
    """
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def main():
    p = 0.1
    n = 100
    n2 = 1000
    l1 = list()
    l2 = list()
    for r in range(0, 100):
        l1.append(pfun(p, r, n) * bibi(r, n))
        l2.append(pfun(p, r, n2) * bibi(r, n2))
    plt.grid(True)
    plt.plot(l1)
    plt.plot(l2)
    plt.yscale('log')
    plt.show()


main()
