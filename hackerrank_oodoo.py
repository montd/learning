#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'toolchanger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY tools
#  2. INTEGER startIndex
#  3. STRING target
#

def toolchanger(tools, startIndex, target):
    # Write your code here
    numberOfTools = len(tools)
    targerIndex = tools.index(target)
    print(numberOfTools, tools, target,startIndex,
                                    targerIndex)
    rightDirection = len(tools[startIndex:targerIndex])
    print(rightDirection)
    iterator = startIndex
    leftDirection = 0
    while (tools[iterator]!=target):
        iterator-=1
        leftDirection+=1
    print(iterator)
    print(leftDirection)
    if (leftDirection < rightDirection):
        return leftDirection
    else: return rightDirection

    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tools_count = 4

    tools = ['ballendmill', 'facemill', 'keywaycutter', 'slotdrill']

    # for _ in range(tools_count):
    #     tools_item = input()
    #     tools.append(tools_item)

    startIndex = 1

    target = 'slotdrill'

    result = toolchanger(tools, startIndex, target)
