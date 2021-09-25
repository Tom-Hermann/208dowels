#!/usr/bin/python3
##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-208dowels-tom.hermann
## File description:
## main
##

from sys import argv
from src.constante import FIT_INDEX, FIT_VALIDITY
from src.error import error
from src.calcul import calcul_tx, calcul_khi

def concat_index(index):
    for i in range(len(index)):
        if (len(index[i]) != 1):
            if (i != len(index) - 1):
                index[i] = index[i][0] + '-' + index[i][-1]
            else:
                index[i] = index[i][0] + '+'
        else:
            index[i] = index[i][0]
    return index


def concat_tab(values, tx):
    index = [[str(i)] for i in range(9)]
    index[-1] = ["8+"]
    res = values
    i  = 0
    while i != len(index):
        while res[i] < 10:
            if (i != 0 and res[i - 1] < res[i + 1]):
                i -= 1
            tx[i] += tx[i + 1]
            tx.pop(i + 1)
            res[i] += res[i + 1]
            res.pop(i + 1)
            index[i].append(index[i + 1][-1])
            index.pop(i + 1)
        i += 1
    index = concat_index(index)
    tx[-1] = 100 - sum(tx[:-1])
    return index, res, tx

def print_tab(index, concat, tx):
    print('   x\t', end='')
    for i in index:
        print("| {}\t".format(i), end='')
    print("| Total")
    print('  Ox\t', end='')
    for i in concat:
        print("| {}\t".format(i), end='')
    print("| {}".format(sum(concat)))
    print('  Tx\t', end='')
    for i in tx:
        print("| {:.1f}\t".format(i), end='')
    print("| {}".format(int(sum(tx))))

def print_fit_validity(v, khi):
    print("Fit validity:\t\t", end='')
    for i in range(len(FIT_VALIDITY[v])):
        if (khi < FIT_VALIDITY[v][i]):
            if (i == 0):
                print("P > {}%".format(FIT_INDEX[i]))
                return
            else:
                print("{}% < P < {}%".format(FIT_INDEX[i], FIT_INDEX[i - 1]))
                return
    print("P < {}%".format(FIT_INDEX[-1]))

def main():
    error(argv[1:])
    values = [int(x) for x in argv[1:]]
    proba = sum([i * values[i] for i in range(len(values))]) / 10 ** 4
    tx = calcul_tx(proba)
    index, concat, tx = concat_tab(values, tx)
    khi = calcul_khi(concat, tx)
    print_tab(index, concat, tx)
    print("Distribution:\t\tB(100, {:.4f})".format(proba))
    print("Chi-squared:\t\t{:.3f}".format(khi))
    print("Degrees of freedom:\t{}".format(len(index) - 2))
    print_fit_validity(len(index) - 3, khi)
    exit(0)

if __name__ == "__main__":
    main()
