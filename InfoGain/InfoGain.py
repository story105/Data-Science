import math

#valueSplit is a list of 2 items. The first is number of positive examples,
#the second is the number of negative examples
def calcEntropy(valueSplit):
    h = 0.0
    probabilityP = valueSplit[0]
    probabilityN = valueSplit[1]
    totalValues = probabilityN + probabilityP
    probabilityP = probabilityP/totalValues
    probabilityN = probabilityN/totalValues
	
    h = -probabilityP * math.log2(probabilityP) - probabilityN * math.log2(probabilityN)
    #fill this in
    return h

#rootValues is a list of the values at the parent node. It consists of 2 items.
#The first is number of positive examples,
#the second is the number of negative examples
#descendantValues is a list of lists.  Each inner list consists of the number of positive
#and negative examples for the attribute value you want to split on.
def calcInfoGain(rootValues, descendantValues):
    gain = 0.0
    totalValues = 0.0
    totalEnt = calcEntropy(rootValues)
    
    for node in descendantValues:
        totalValues += sum(node) / sum(rootValues) * calcEntropy(node)

    gain = totalEnt - totalValues
    
    return gain



if __name__ == "__main__":
	attributeName = "Humidity"
	rootSplit = [9,5] # 9 positive, 5 negative examples
	descendantSplit = [[3,4],[6,1]]
	
	ig = calcInfoGain(rootSplit, descendantSplit)
	print("The information gain of splitting on ",attributeName," is: ",ig," bits")