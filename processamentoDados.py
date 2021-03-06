#read data from a file in the format: int\nint\nint\n...

import math
import os
import matplotlib.pyplot
from plotting import *

### functions ###

def fileToIntList(file):
    vector = file.read()
    holder = ""
    numbersList = list()
    for i in vector:
        if i == "\n":
            numbersList.append(int(holder))
            holder = ""
        else:
            holder = holder + i
    return numbersList

def mean(numbersList):
    accumulator = 0
    for i in numbersList:
        accumulator = accumulator + i
    accumulator = accumulator / len(numbersList)
    return accumulator

def maximum(numbersList):
    myMax = 0
    for i in numbersList:
        if i > myMax:
            myMax = i
    return myMax

def minimum(numbersList):
    myMin = 999999999 #which number to use as max?
    for i in numbersList:
        if i < myMin:
            myMin = i
    return myMin

def rms(numbersList):
    accumulator = 0
    for number in numbersList:
        accumulator = accumulator+number*number
    return math.sqrt(accumulator)
###########################################################################


