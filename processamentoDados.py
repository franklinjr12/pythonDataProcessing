#read data from a file in the format: int\nint\nint\n...

import math
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

###########################################################################




myFile = open("coletasDispositivo\\semSensor1540954526", 'r')

numbersList = fileToIntList(myFile)


x = domain(0, len(numbersList)-1, 1)
y = numbersList


matplotlib.pyplot.figure(1)
myPlot(x,y)

print("Media: " + str(mean(y)))


##myFile = open("coletasDispositivo\\comSensorSemCarga1539052914", 'r')
##numbersList = fileToIntList(myFile)
##y = numbersList
##matplotlib.pyplot.figure(2)
##myPlot(x,y)
##
##
##myFile = open("coletasDispositivo\\ferroSolda34W1539053092", 'r')
##numbersList = fileToIntList(myFile)
##y = numbersList
##matplotlib.pyplot.figure(3)
##myPlot(x,y)


matplotlib.pyplot.show()


print(maximum(y))



##print(numbersList)
##
##print("Mean of the numbers: " + str(mean(numbersList)))
##
##print("Larger number: " + str(maximum(numbersList)))
##
##print("Lesser number: " + str(minimum(numbersList)))
