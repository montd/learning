#!/bin/python3

import math
import os
import random
import re
import sys

def get(data):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    nm = [n,m]
    # print(nm)
    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)
    return nm,matrix

def load():
    with open('matrix_test.txt','r') as f:
        data = f.read()
    dataFirstProcess = [[x for x in y] for y in data.split('\n') ]
    columnAndRow = dataFirstProcess.pop(0)
    columnAndRow.remove(' ')
    columnAndRow = [int(i) for i in columnAndRow]
    return columnAndRow, dataFirstProcess

def matrix(columnAndRow, dataFirstProcess):
    print(columnAndRow)
    print(dataFirstProcess)
    decoded =''
    for n in range(columnAndRow[1]):
        for m in range(columnAndRow[0]):
            decoded += dataFirstProcess[m][n]



    print(decoded)
    # print(decodedCleaned)


    # for i in dataFirstProcess:
nm, code = load()
# nm, code = get(data)
matrix(nm,code)
