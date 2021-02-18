import pandas as pd
import numpy as np

def accuracy(predicted, actual):
	correct = 0
	for i in range(len(predicted)):
		if predicted[i] == actual[i]:
			correct += 1

	print('Number of Docs: ', len(actual))
	print('Number of correctly predicted: ', correct)
	return ((correct*100)/len(actual))

def toFile(predictedList, size):
	#writing to file (CSV)
	index = size
	row = []
	for i in predictedList:
		row.append([index, i])
		index += 1
		
	finalOutput = pd.DataFrame(data = row, columns = ['id', 'class'])
	finalOutput.to_csv('data/actual.csv', index=False)

def getFilesReady():
	df = pd.read_csv('data/training.csv', index_col = False, header = None)
	size = (3 * df.shape[0])//4
	Actualdata = df.iloc[size:, -1]
	toFile(Actualdata, size)
	print('Done')
	
def findConfusionValue(matrix):
	#Creating confusion matrix
	for i in range(matrix.shape[0]):
		for j in range(matrix.shape[1]):
			if i == j:
				matrix[i, j] = 0
	
	totalConfusedValues = []
	matrix = np.transpose(matrix)
	for i in range(matrix.shape[0]):
		totalConfusedValues.append(sum(matrix[i]))
	return totalConfusedValues
	

if __name__ == '__main__':
	predictedData = pd.read_csv('data/predictedc.csv')

	confusionMatrix = np.zeros([20, 20])
	predicted = predictedData.iloc[1:, -1].tolist()
	print('Getting file')
	#getFilesReady()
	actual = pd.read_csv('data/actual.csv')
	actual = actual.iloc[1:, -1].tolist()

	for i in range(len(actual)):
		confusionMatrix[predicted[i]-1, actual[i]-1] += 1

	print(confusionMatrix)
	np.save('data/confusionMatrix',confusionMatrix)
	
	print(findConfusionValue(confusionMatrix))
	print('Accuracy: ', accuracy(predicted, actual))