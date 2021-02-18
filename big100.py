import pandas as pd
import copy

def changeWord(list):
	r1 = [105, 112, 145, 151, 103, 122, 132, 109, 111, 142, 104, 153, 161, 119, 138, 120, 126, 113, 101, 129]
	r2 = [40, 57, 67, 72, 48, 32, 76, 91, 9, 16, 2, 22, 43, 38, 89, 94, 55, 27, 84, 6]
	for i in range(20):
		list[r2[i]] = list[r1[i]]
	return list


def greatSort(list):
	ind = []
	for i in range(100):
		max = list[i]
		flag = 0
		for j in range(i, len(list)):
			if list[j] > max:
				max = list[j]
				temp = list[i]
				list[i] = list[j]
				list[j] = temp
				flag = copy.deepcopy(j)

		ind.append(flag)
	return ind


def loadData(filename):
	data = pd.read_csv(filename, header = None)
	return data


data = loadData('data/wordIG.csv')
data = data.iloc[:, :]
column = data.iloc[:, -1].tolist()

valueList = []
indexList = []
for index, row in data.iterrows():
	valueList.append(row[0])
	indexList.append(index)

wordid = greatSort(valueList)
#wordid = changeWord(wordid)
words = loadData('data/voc.csv')

wordList = []
for index, row in words.iterrows():
	for i in wordid:
		if i == index:
			wordList.append(row[0])

print(wordList)


