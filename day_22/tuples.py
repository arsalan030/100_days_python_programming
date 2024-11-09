from collections import OrderedDict

# Initializing tuple 
test_tup = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])

# printing original tuple 
print("The original tuple is : " + str(test_tup))

# Remove duplicate lists in tuples(Preserving Order)
# Using OrderedDict() + tuple()
res = list(OrderedDict((tuple(x), x) for x in test_tup).values())

# printing result
print("The unique lists tuple is : " + str(res))
'''
 test_list = [(15, 3), (3, 9)] 
Output : [9, 5, 3, 1]


'''


test_list = [(15, 5,5), (3, 9),(3,9)]
x = ""

extarct_digit = set((tuple(map(int,str(i))) for  val in test_list for i in val))
print(extarct_digit)



'''

Python  Cross Pairing in Tuple List
'''
test_list1 = [(1, 7), (6, 7), (8, 100), (4, 21)]
test_list2 = [(1, 3), (2, 1), (9, 7), (2, 17)] 

test_list = [(t1[1],t2[1])for  t1,t2 in zip(test_list1,test_list2)if t1[0]==t2[0]]
print(test_list)


# Python3 code to demonstrate working of
# Flatten tuple of List to tuple
# Using sum() + tuple()

# initializing tuple
test_tuple = ([5, 6], [6, 7, 8, 9], [3])

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Flatten tuple of List to tuple
# Using sum() + tuple()
res = tuple(sum(test_tuple,[]))

# printing result
print("The flattened tuple : " + str(res))


# Python3 code to demonstrate working of
# Summation combination in tuple lists
# Using nested for loops

# Initialize list
test_list = [(2, 4), (6, 7), (5, 1), (6, 10)]

# Printing original list
print("The original list : " + str(test_list))

# Summation combination in tuple lists
# Using nested for loops
res = []
for i in range(len(test_list)):
	for j in range(i+1, len(test_list)):
		res.append((test_list[i][0]+test_list[j][0],
					test_list[i][1]+test_list[j][1]))

# Printing result
print("The Summation combinations are : " + str(res))


from itertools import accumulate

nums = [1, 2, 3, 4]
print(list(accumulate(nums)))  
# Output: [1, 3, 6, 10]

import itertools

# Input list
test_list = [(2, 4), (6, 7), (5, 1), (6, 10)]

# Printing input list for understanding
print("The original list : " + str(test_list))

xres = list(map(lambda x: (x[0][0]+x[1][0], x[0][1] +
						x[1][1]), itertools.combinations(test_list, 2)))

# Printing the resultant list
print("The Summation combinations are : " + str(res))



# Python3 code to demonstrate working of
# Custom sorting in list of tuples
# Using sorted() + lambda

# Initializing list
test_list = [(7, 8), (5, 6), (7, 5), (10, 4), (10, 1)]

# printing original list
print("The original list is : " + str(test_list))

# Custom sorting in list of tuples
# Using sorted() + lambda
res = sorted(test_list, key = lambda sub: (-sub[0], sub[1]))

# printing result
print("The tuple after custom sorting is : " + str(res))




lst = [(7, 8), (5, 6), (7, 5), (10, 4), (10, 1)]
n = len(lst)

for i in range(n):
	for j in range(n-i-1):
		if lst[j][0] < lst[j+1][0] or (lst[j][0] == lst[j+1][0] and lst[j][1] > lst[j+1][1]):
			lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)


test_tup = (5, 6, 7)

k = "Gfg"
test_k  = [ele for i in test_tup for ele in (i,k)]
print(test_k)

'''
test_list = [[(4, 5), (7, 8)], [(10, 13), (18, 17)]] 
Output : [(4, 7, 10, 18), (5, 8, 13, 17)] 
Explanation : All column number elements contained together.
'''
test_list = [[(4, 5), (7, 8)], [(10, 13), (18, 17)]] 

all_coulms = [tuple(i[0] for i in val )for  idx ,val in enumerate(test_list)] +[tuple(i[1] for i in val )for  idx ,val in enumerate(test_list)]
print(all_coulms)




      








