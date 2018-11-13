from processamentoDados import *
import time


tempoAmostragem = 24 #horas


def cModificationTimeToList(cStrTime):
	fileTime = list()
	fileTime.append(cStrTime[11])
	fileTime.append(cStrTime[12])
	fileTime.append(cStrTime[14])
	fileTime.append(cStrTime[15])
	fileTime.append(cStrTime[17])
	fileTime.append(cStrTime[18])	
	return fileTime



# arquivo  = "rodando2//casaFds1541808317"

# lastModified = str(time.ctime(os.path.getmtime(arquivo)))

# print("last modified: %s" % lastModified)

counter = 0

dataResult = list()
dataTime = list()
data = list()
dataResult.append(dataTime) #posicao 1 -> tempo
dataResult.append(data) 	#posicao 2 -> dado

folderName = "rodando2"

firstTime = 0

print("Setting first time")

for filename in os.listdir(folderName):
	myFile = open(folderName+"\\"+str(filename), 'r')
	result =  cModificationTimeToList(str(time.ctime(os.path.getmtime(folderName+"\\"+str(filename)))))
	string = ""
	for letter in result:
		string = string+letter
	firstTime = int(string)
	break

print("first time setted")


print("Start processing")

for filename in os.listdir(folderName):


	myFile = open(folderName+"\\"+str(filename), 'r')

	numbersList = fileToIntList(myFile)

	result =  cModificationTimeToList(str(time.ctime(os.path.getmtime(folderName+"\\"+str(filename)))))
	string = ""
	for letter in result:
		string = string+letter
	modificationTime =  int(string)

	deltaT = modificationTime - firstTime

	for number in numbersList:
		dataResult[1].append(number)

	# if(deltaT < 0):
	# 	break
	# else:
	# 	dataResult[0].append(deltaT) #armazena a hora
	# 	dataResult[1].append(mean(numbersList)) #armazena a media daquela hora
		# for number in numbersList:	
		# 	dataResult[0].append(deltaT) #armazena a hora
		# 	dataResult[1].append(number) #armazena a media daquela hora
#		continue
#	break




	# counter = counter+1


print("End processing")


print("Plotting")


#myPlot(dataResult[0], dataResult[1])

myPlot(range(len(dataResult[1])), dataResult[1])



matplotlib.pyplot.show()

#print(dataResult[0])
