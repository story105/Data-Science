import math

NUM_ATTRIBUTES = 2
TRAIN_DATA_FILE = "reg_train.csv"


#read the train file and return the data as two lists (ind and dep variables)
def readData(fname):
	data = []
	x = []
	y = []
	f = open(fname,"r")
	for i in f:
		instance = i.split(",")
		x.append(float(instance[0].strip()))
		y.append(float(instance[1].strip()))

	f.close()
	data.append(x)
	data.append(y)
	return data

def printParams(params):
	print("The value of B0 (intercept) is: ", params[0])
	print("The value of B1 (slope) is: ", params[1])

#The linear regression algorithm. Takes a list of lists as input
def lreg(ind_variable,dep_variable):
	params = []
	B0 = 0.0
	B1 = 0.0
	
	xbar = sum(ind_variable)/len(ind_variable)   
	ybar = sum(dep_variable)/len(dep_variable)
    
	num = 0.0
	den = 0.0
    
	for i in range(len(dep_variable)):
		num += ind_variable[i] * (dep_variable[i]-ybar)
		den += ind_variable[i] * (ind_variable[i]-xbar)
	B1 = num/den
	B0 = ybar - B1*xbar
    


	params.append(B0)
	params.append(B1)
	return params


#this is the main routine of the program. You should not have to modify anything here
if __name__ == "__main__":
	train_matrix = readData(TRAIN_DATA_FILE)
	parameters = lreg(train_matrix[0],train_matrix[1])
	printParams(parameters)
