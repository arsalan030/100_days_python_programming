
# Function to check if string follows order of 
# characters defined by a pattern 
from collections import OrderedDict 

def checkOrder(input, pattern): 
	
	# create empty OrderedDict 
	# output will be like {'a': None,'b': None, 'c': None} 
	dict = OrderedDict.fromkeys(input) 
	print(dict['e'])

	# traverse generated OrderedDict parallel with 
	# pattern string to check if order of characters 
	# are same or not 
	ptrlen = 0
	for key,value in dict.items(): 
		if (key == pattern[ptrlen]): 
			ptrlen = ptrlen + 1
		
		# check if we have traverse complete 
		# pattern string 
		if (ptrlen == (len(pattern))): 
			return 'true'

	# if we come out from for loop that means 
	# order was mismatched 
	return 'false'

# Driver program 
if __name__ == "__main__": 
	input = 'engineers rock'
	pattern = 'er'
	print (checkOrder(input,pattern)) 



# Function to find common elements in three
# sorted arrays
from collections import Counter

'''
    8. Find Common Elements in Three Sorted Arrays by Dictionary Intersection
        ◦ Use dictionary intersection to find common elements in three sorted arrays.
       Input:
       python
       Copy code
       arr1 = [1, 2, 3, 4, 5]
       arr2 = [1, 2, 5, 7, 9]
       arr3 = [1, 3, 4, 5, 8]
       Expected Output:
       python
       Copy code
       [1, 5]
'''
def commonElement(ar1,ar2,ar3):
	# first convert lists into dictionary
	ar1 = Counter(ar1)
	ar2 = Counter(ar2)
	ar3 = Counter(ar3)
	
	# perform intersection operation
	resultDict = dict(ar1.items() & ar2.items() & ar3.items())
	print(resultDict)
	common = []
	
	# iterate through resultant dictionary
	# and collect common elements
	for (key,val) in resultDict.items():
		for i in range(0,val):
			common.append(key)

	print(common)

# Driver program
if __name__ == "__main__":
	ar1 = [1, 5, 10, 20, 40, 80]
	ar2 = [6, 7, 20, 80, 100]
	ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
	commonElement(ar1,ar2,ar3)
	


# Function to find winner of an election where votes 
# are represented as candidate names 
from collections import Counter 

def winner(input): 

	# convert list of candidates into dictionary 
	# output will be likes candidates = {'A':2, 'B':4} 
	votes = Counter(input) 
	
	# create another dictionary and it's key will 
	# be count of votes values will be name of 
	# candidates 
	dict = {} 

	for value in votes.values(): 

		# initialize empty list to each key to 
		# insert candidate names having same 
		# number of votes 
		dict[value] = [] 

	for (key,value) in votes.items(): 
		dict[value].append(key) 

	# sort keys in descending order to get maximum 
	# value of votes 
	maxVote = sorted(dict.keys(),reverse=True)[0]

	# check if more than 1 candidates have same 
	# number of votes. If yes, then sort the list 
	# first and print first element 
	if len(dict[maxVote])>1: 
		print (sorted(dict[maxVote])[0])
	else: 
		print (dict[maxVote][0]) 

# Driver program 
if __name__ == "__main__": 
	input =['john','johnny','jackie','johnny',
			'john','jackie','jamie','jamie',
			'john','johnny','jamie','johnny',
			'john'] 
	winner(input) 




			
				


	
	
