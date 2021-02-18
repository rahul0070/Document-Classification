import pandas as pd 
import numpy as np 
import math

def calculateProbList(list):
	result = []
	for i in range(1,21):
		result.append(list[i]/list[0])
	return result

def loadData(filename):
	try:
		print('Loading Data.')
		data = pd.read_csv(filename, index_col = False, header = None)
		print('Done.')
	except:
		print('ERROR. CSV file not found.')

	return data

def entropy(probability):
	return (probability * math.log(probability))

def findTotalIg(MLE_list):
	result = []
	for i in MLE_list:
		result.append(i * math.log(i))
	return sum(result)

def getWordProbability(index):
	p1 = []
	p2 = []
	for i in range(20):
		dl = MAP[index]
		value = MAP[index][i]
		if value == 0:
			value = 0.0000000000001
		p1.append(value * math.log(value))
		p2.append((1-value) * math.log((1-value)))
	return sum(p1), sum(p2)
	

def getWordProbability1(df):
	present = []
	notPresent = []
	pr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	
	for i in range(20):
		total = 0
		for index, row in df.iterrows():
			if row[1] == i+1 and row[0]!= 0:
				total += 1
		if total == 0:
			total = 0.0001
		probability = total/df.shape[0]
		present.append(probability * math.log(probability))
		notPresent.append((1-probability) * math.log(1-probability))

	return sum(present), sum(notPresent)

if __name__ == '__main__':
	data = loadData('data/samplTraining.csv')
	# Contains all probabilities of all words.
	wordProbability = np.load('data/wordProb.npy')
	wordProbability = wordProbability.tolist()
	column = data.shape[1]
	classDistribution = [12000, 483, 624, 622, 643, 602, 630, 618, 614, 649, 628, 646, 639, 626, 621, 637, 651, 580, 593, 467, 427]
	probList = calculateProbList(classDistribution)
	totalIG = findTotalIg(probList)
	MAP = np.load('data/trained.npy')
	MAP = MAP.tolist()
	inp = input(len(wordProbability))
	wordIG = []
	for i in range(len(MAP)):
		print(i)
		dataTemp = data.iloc[:, [i, -1]]
		dataTemp.columns = ['id', 'Class']
		p1, p2 = getWordProbability(i)
		IG = (-totalIG) + (wordProbability[i]) * p1 + (1 - wordProbability[i]) * p2
		wordIG.append(IG)

	print(wordIG)
	np.save('data/wordIG', wordIG)