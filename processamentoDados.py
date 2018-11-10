#======================================================================================================================
# --- Processa toda uma pasta de dados ---

# media = 0
# maximum = 0
# minimum = 256
# i = 1

# for filename in os.listdir("rodando"):
# 	myFile = open("rodando\\"+str(filename), 'r')

# 	numbersList = fileToIntList(myFile)

# 	x = domain(0, len(numbersList)-1, 1)
# 	y = numbersList
# 	actualMean = mean(y)
# 	media = media + actualMean
# 	i = i+1
# 	if actualMean > maximum:
# 		maximum = actualMean
# 	if actualMean < minimum:
# 		minimum = actualMean

# print("Resultados: ")

# print("Media: " + str(media/i))

# print("Maximo: " + str(maximum))

# print("minimo: " + str(minimum))

#======================================================================================================================




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

###########################################################################




myFile = open("rodando\\noiteToda1540993982", 'r')

numbersList = fileToIntList(myFile)

media = mean(numbersList)	
i = 0
for e in numbersList:
	numbersList[i] = numbersList[i] - media
	i = i+1


x = domain(0, len(numbersList)-1, 1)
y = numbersList

matplotlib.pyplot.figure(1)

myPlot(x,y)

print("Rodando: ")

print("Media: " + str(mean(y)))

print("Maximo: " + str(maximum(y)))

matplotlib.pyplot.show()




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