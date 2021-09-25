##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-208dowels-tom.hermann
## File description:
## calcul
##

from math import factorial

def calcul_proba(value):
    return sum([i * value[i] for i in range(len(value))]) / 10 ** 4

def binomial_distribution(k, n):
    return factorial(n) / (factorial(k) * factorial(n - k))

def calcul_tx(binomial):
    value = [i for i in range(9)]
    return [100 * binomial_distribution(i, 100) * binomial ** i * (1 - binomial) ** (100 - i) for i in value]

def calcul_khi(Ox, Tx):
    res = 0
    for i in range(len(Ox)):
        res += (Ox[i] - Tx[i]) ** 2 / Tx[i]
    return res
