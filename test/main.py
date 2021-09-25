#!/usr/bin/python3
##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-208dowels-tom.hermann
## File description:
## main
##

import unittest
from src.calcul import *
from src.main import concat_index, main
from src.error import error
import sys
import io

# self.assertRaises.exception.code

class TestStringMethods(unittest.TestCase):

    list_1 = [6, 4, 10, 18, 20, 19, 11, 5, 7]
    list_2 = [6, 4, 10, 8, 20, 19, 11, 5, 17]
    list_3 = [4, 5, 13, 19, 20, 16, 12, 7, 4]

    argv_1 = ["6", "4", "10", "18", "20", "19", "11", "5", "7"]
    argv_2 = ["6", "4", "10", "8", "20", "19", "11", "5", "17"]
    argv_3 = ["4", "5", "13", "19", "20", "16", "12", "7", "4"]

    error_argv_1 = ["4", "5", "13", "19", "20", "16", "12", "7"]
    error_argv_2 = ["4", "5", "13", "19", "20", "16", "12.3", "7", "4.0"]
    error_argv_3 = []
    error_argv_4 = ["4", "5", "13", "19", "20", "16", "12", "7", "4", "1"]

    help_argv_1 = ["-h"]
    help_argv_2 = ["4", "5", "13", "19", "20", "16", "12", "-h"]
    help_argv_3 = ["4", "5", "13", "19", "20", "16", "12", "7", "4", "-h"]

    index_1 = [['0', '1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7', '8+']]
    index_concat_1 =['0-1', '2', '3', '4', '5', '6', '7+']

    index_2 = [['0', '1'], ['2', '3'], ['4'], ['5'], ['6', '7'], ['8+']]
    index_concat_2 = ['0-1', '2-3', '4', '5', '6-7', '8+']

    index_3 = [['0', '1', '2'], ['3'], ['4'], ['5'], ['6'], ['7', '8+']]
    index_concat_3 = ['0-2', '3', '4', '5', '6', '7+']

    def test_help(self):
        sys.stdout = io.StringIO()
        with self.assertRaises(SystemExit) as cm:
            error(self.help_argv_1)
        self.assertEqual(cm.exception.code, 0)
        with self.assertRaises(SystemExit) as cm:
            error(self.help_argv_2)
        self.assertEqual(cm.exception.code, 0)
        with self.assertRaises(SystemExit) as cm:
            error(self.help_argv_3)
        self.assertEqual(cm.exception.code, 0)
        sys.stdout = sys.__stdout__
        print("Test help: OK")

    def test_error(self):
        with self.assertRaises(SystemExit) as cm:
            error(self.error_argv_1)
        self.assertEqual(cm.exception.code, 84)
        print("Test Error: Not enough argument: OK")
        with self.assertRaises(SystemExit) as cm:
            error(self.error_argv_2)
        self.assertEqual(cm.exception.code, 84)
        print("Test Error: Float Argument: OK")
        with self.assertRaises(SystemExit) as cm:
            error(self.error_argv_3)
        self.assertEqual(cm.exception.code, 84)
        print("Test Error: No Argument: OK")
        with self.assertRaises(SystemExit) as cm:
            error(self.error_argv_4)
        self.assertEqual(cm.exception.code, 84)
        print("Test Error: To Many Argument: OK")


    def test_proba(self):
        self.assertAlmostEqual(0.0410, calcul_proba(self.list_1))
        self.assertAlmostEqual(0.0460, calcul_proba(self.list_2))
        self.assertAlmostEqual(0.0401, calcul_proba(self.list_3))
        print("Test proba: OK")

    def test_concat_index(self):
        self.assertEqual(concat_index(self.index_1), self.index_concat_1)
        self.assertEqual(concat_index(self.index_2), self.index_concat_2)
        self.assertEqual(concat_index(self.index_3), self.index_concat_3)
        print("Test Concat Index: OK")


    def test_calcul_tx(self):
        self.assertEqual(calcul_tx(0.0410), [1.5200599518975109, 6.498692182252132, 13.752967449302092, 19.207307337954745, 19.91331107482952, 16.345942104385607, 11.064901719948198, 6.352470017679185, 3.1571908468992094])
        self.assertEqual(calcul_tx(0.0460), [0.901233798361773, 4.345571774071442, 10.37197791358561, 16.337133624893063, 19.102801424075693, 17.685109242917875, 13.501734345134714, 8.742362879359465, 4.900396802659826])
        self.assertEqual(calcul_tx(0.0401), [1.6695489910642731, 6.974571782652083, 14.422519283232893, 19.681778059953675, 19.93859050937645, 15.992415465130865, 10.578030127168807, 5.934074496056152, 2.8818033152076])
        print("Test Tx: OK")

if __name__ == '__main__':
    unittest.main()