# python program extarct digit form tuple list

test_list= [(1,5),(3,9)]
strr = [int(' '.join(str(i)))for ii in test_list  for i in ii]
print(strr)

'''
convert tuple in to tuple pair
'''
tuples = ('A', 'B', 'C')
pair_tuples = [(tuples[0],i)for i in tuples[1:]]
print(pair_tuples)


# Python3 code to demonstrate working of 
# Convert Tuple to Tuple Pair
# Using product() + next()
from itertools import product

# initializing tuple
test_tuple = ('G', 'F', 'G')

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Convert Tuple to Tuple Pair
# Using product() + next()
test_tuple = iter(test_tuple)
res = list(product(next(test_tuple), test_tuple))

# printing result 
print("The paired records : " + str(res))


'''

Python  Convert Nested Tuple to Custom Key Dictionary

'''

test_tuple = ((1, 'Gfg', 2), (3, 'best', 4))
keys = ['key', 'value', 'id']


dicts = [{v:k for k,v  in zip(val ,keys)}for val in test_tuple]
print(dicts)


# Python3 code to demonstrate working of 
# Extract Symmetric Tuples
# Using dictionary comprehension + set()

# initializing list
test_list = [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]

# printing original list
print("The original list is : " + str(test_list))

# Extract Symmetric Tuples
# Using dictionary comprehension + set()
temp = set(test_list) & {(b, a) for a, b in test_list}
res = {(a, b) for a, b in temp if a < b}

# printing result 
print("The Symmetric tuples : " + str(res)) 


# Python3 code to demonstrate working of 
# Extract Symmetric Tuples
# Using Counter() + list comprehension
from collections import Counter

# initializing list
test_list = [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]

# printing original list
print("The original list is : " + str(test_list))

# Extract Symmetric Tuples
# Using Counter() + list comprehension<
temp = [(sub[1], sub[0]) if sub[0] < sub[1] else sub for sub in test_list]
cnts = Counter(temp)
res = [key for key, val in cnts.items() if val == 2]

# printing result 
print("The Symmetric tuples : " + str(res)) 


'''
Python program to Sort Tuples by their Maximum element
'''
test_list = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)] 

test = sorted(test_list,reverse=True)
print(test)


# Python3 code to demonstrate working of 
# Sort Tuples by Maximum element
# Using max() + sort()

# helper function
def get_max(sub):
	return max(sub)

# initializing list
test_list = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]

# printing original list
print("The original list is : " + str(test_list))

# sort() is used to get sorted result
# reverse for sorting by max - first element's tuples
test_list.sort(key = get_max, reverse = True)

# printing result 
print("Sorted Tuples : " + str(test_list))

test_tuple = (5, (6, (7, 8, 6))) 
test = test_tuple[1][1]
print(test)




# Python3 code to demonstrate working of 
# Elements Frequency in Mixed Nested Tuple
# using recursion + Counter()
from collections import Counter

# Helper function
def flatten(test_tuple):

	for tup in test_tuple:
		if isinstance(tup, tuple):
			yield from flatten(tup)
		else:
			yield tup

# Initializing tuple
test_tuple = (5, 6, (5, 6), 7, (8, 9), 9)

# Printing original tuple
print("The original tuple : " + str(test_tuple))

# Elements Frequency in Mixed Nested Tuple
# using recursion + Counter()
res = dict(Counter(flatten(test_tuple)))

# Printing result 
print("The elements frequency : " + str(res))

test_tup1 = (3, 4),
test_tup2 = (5, 6),


test_tup1 +=test_tup2
print(test_tup1)