from processamentoDados import *




#--- Processa toda uma pasta de dados ---
media = 0
maximumMean = 0
maximumMean = 256
i = 1

yData = list()

folderName = "rodando2"


for filename in os.listdir(folderName):
	myFile = open(folderName+"\\"+str(filename), 'r')

	numbersList = fileToIntList(myFile)

	for numbers in numbersList:
		yData.append(numbers)

	x = domain(0, len(numbersList)-1, 1)
	y = numbersList
	actualMean = mean(y)
	media = media + actualMean
	i = i+1
	if actualMean > maximumMean:
		maximumMean = actualMean
	if actualMean < maximumMean:
		maximumMean = actualMean

print("Resultados: ")

print("Media: " + str(media/i))

print("Maior valor de media: " + str(maximumMean))

print("Menor valor de media: " + str(maximumMean))


x = list(range(len(yData)))

myPlot(x,yData)

matplotlib.pyplot.show()
