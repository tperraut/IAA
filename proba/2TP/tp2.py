#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt

def pfun(p, r, N):
    """
        Calcul de la concentration de mesure
    """
    return ((p ** r) * ((1 - p) ** (N - r)))

def bibi(r, N):
    """
        Calcul coefficient binomial
    """
    return (math.factorial(N) / (math.factorial(r) * math.factorial(N - r)))

def main():
    p = 0.1
    N = 100
    N2 = 1000
    l1 = list()
    l2 = list()
    for r in range(0, 100):
        l1.append(pfun(p, r, N) * bibi(r, N))
        l2.append(pfun(p, r, N2) * bibi(r, N2))
    plt.grid(True)
    plt.plot(l1)
    plt.plot(l2)
    plt.yscale('log')
    plt.show()


main()
