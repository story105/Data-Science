import math

NUM_ATTRIBUTES = 4
TRAIN_DATA_FILE = "sample_train.csv"
TEST_DATA_FILE = "sample_test.csv"

#read the train file and return the data matrix and the target variable to predict
def readData(fname):
	data = []
	labels = []
	f = open(fname,"r")
	for i in f:
		instance = i.split(",")
		vector = []
		for j in range(NUM_ATTRIBUTES):
			vector.append(float(instance[j]))
		data.append(vector)
		labels.append(instance[NUM_ATTRIBUTES])
	f.close()
	return [data,labels]

#compute the dot product of vectors represented as lists
def dotProduct(vecA,vecB):
	sum = 0.0
	for i in range(NUM_ATTRIBUTES):
		sum += vecA[i]*vecB[i]
	return sum

#compute the cosine similarity of 2 vectors represented as lists
def cosDistance(vecA,vecB):
	normA = math.sqrt(dotProduct(vecA,vecA))
	normB = math.sqrt(dotProduct(vecB,vecB))
	return dotProduct(vecA,vecB)/(normA*normB) 
	
#compare predicted labels to truth labels. Identify errors and print accuracy
def printAccuracy(pred,truth):
	total = 0.0
	correct= 0.0
	for i in range(len(pred)):
		total += 1.0
		if pred[i]==truth[i]:
			correct += 1.0
		else:
			print("Predicted that test point ",i," was ",pred[i], "but it is actually ",truth[i])
	print("The accuracy is: ", 100*(correct/total), " percent")
	
#The KNN algorithm. Predicts the label for each test data set instance and adds to a list. Returns the list as output
def knn(train_data, train_labels, test_data): # labels is seteosa/etc
	predictions = []
	vector_list = []
	#iterate through the test data, compare to train data, return the train_labels
	for data in test_data:
		vector_list = []
		counter = 0
		for train in train_data:
			distance = cosDistance(train, data)
			vector_list.append((counter, distance))  # so it keeps the respective flower thing
			counter += 1  # counter mimics the list of test data

		max_count = 0
		for x in range(len(vector_list)):
			prediction = vector_list[x][0]       
			if vector_list[x][1] > max_count:
				max_count = vector_list[x][1]
				final_prediction = vector_list[x][0]
		
		predicted_label = train_labels[final_prediction]
		predictions.append(predicted_label)	
	#implement KNN here
	#for each test data point predict the label and add your prediction to the preditions list
	#compare to every data point in train_data using cosDistance by making a call to the above function
	#find the index, c, of the closest data point

	return predictions


#this is the main routine of the program. You should not have to modify anything here
if __name__ == "__main__":
	train_matrix = readData(TRAIN_DATA_FILE)
	train_data = train_matrix[0]
	train_labels = train_matrix[1]
	test_matrix = readData(TEST_DATA_FILE)
	test_data = test_matrix[0]
	test_labels = test_matrix[1]
	predictions = knn(train_data,train_labels,test_data)
	printAccuracy(predictions,test_labels)
