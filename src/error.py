##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-208dowels-tom.hermann
## File description:
## error
##

from src.constante import FAILURE, SUCCESS

def printUsage():
    print("USAGE\n\t./208dowels O0 O1 O2 O3 O4 O5 O6 O7 O8\n")
    print("DESCRIPTION\n\tOi\tsize of the observed class")

def error(argv):
    if "-h" in  argv or "--help" in argv:
        printUsage()
        exit(SUCCESS)
    if len(argv) != 9:
        exit(FAILURE)
    try:
        if (sum([int(x) for x in argv]) != 100):
            exit(FAILURE)
    except:
        exit(FAILURE)