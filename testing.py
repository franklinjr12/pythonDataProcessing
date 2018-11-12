from processamentoDados import *



tempoAmostragem = 24 #horas




media = 0
maximum = 0
minimum = 256
i = 1

folderName = "rodando2"


for filename in os.listdir(folderName):
	myFile = open(folderName+"\\"+str(filename), 'r')

	numbersList = fileToIntList(myFile)

	x = domain(0, len(numbersList)-1, 1)
	y = numbersList
	actualMean = mean(y)
	media = media + actualMean
	i = i+1
	if actualMean > maximum:
		maximum = actualMean
	if actualMean < minimum:
		minimum = actualMean

print("Resultados: ")

print("Media: " + str(media/i))

print("Maximo: " + str(maximum))

print("minimo: " + str(minimum))