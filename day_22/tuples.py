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

# Python3 code to demonstrate working of 
# Sort Tuples by Total digits
# Using sorted() + lambda + sum() + len()

# initializing list
test_list = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]

# printing original list
print("The original list is : " + str(test_list))

# performing sort, lambda function provides logic
res = sorted(test_list, key = lambda tup : sum([len(str(ele)) for ele in tup ]))

# printing result 
print("Sorted tuples : " + str(res))




# Python3 code to demonstrate working of 
# Convert Tuple Matrix to Tuple List
# Using list comprehension + zip()

# initializing list
test_list = [[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]

# printing original list
print("The original list is : " + str(test_list))

# flattening 
temp = [ele for sub in test_list for ele in sub]

print(temp)

# joining to form column pairs
res = list(zip(*temp))

# printing result 
print("The converted tuple list : " + str(res))


# Python3 code to demonstrate working of 
# Sort by Frequency of second element in Tuple List
# Using sorted() + loop + defaultdict() + lambda
from collections import defaultdict

# initializing list
test_list = [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]

# printing original list
print("The original list is : " + str(test_list))

# constructing mapping
freq_map = defaultdict(int)
for idx, val in test_list:
	freq_map[val] += 1

# performing sort of result 
res = sorted(test_list, key = lambda ele: freq_map[ele[1]], reverse = True)

# printing results
print("Sorted List of tuples : " + str(res))



test_list = [('Gfg', 10), ('best', 3), ('CS', 8), ('Geeks', 7)]
ord_list = ['Geeks', 'best', 'CS', 'Gfg'] 

#ord_list = iter(ord_list)

test_dict = {k:v for k,v in test_list}
new_list = list(map(lambda ele: (ele,test_dict[ele]),ord_list))

print(new_list)

test_dict = {k:v for k,v in test_list}
new_list = [(k,test_dict[k])for k in ord_list]
print(new_list)


# Python3 code to demonstrate working of 
# Order Tuples by List
# Using setdefault() + sorted() + lambda

# initializing list
test_list = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]

# printing original list
print("The original list is : " + str(test_list))

# initializing order list 
ord_list = ['Geeks', 'best', 'CS', 'Gfg']

# Order Tuples by List
# Using setdefault() + sorted() + lambda
temp = dict()
for key, ele in enumerate(ord_list):
	temp.setdefault(ele, []).append(key)	 
res = sorted(test_list, key = lambda ele: temp[ele[0]]) 

# printing result 
print("The ordered tuple list : " + str(res)) 


# Python3 code to demonstrate working of 
# Filter Tuples by Kth element from List
# Using list comprehension

# initializing list
test_list = [("GFg", 5, 9), ("is", 4, 3), ("best", 10, 29)]

# printing original list
print("The original list is : " + str(test_list))

# initializing check_list
check_list = [4, 2, 8, 10]

# initializing K 
K = 1

# checking for presence on Kth element in list 
# one liner 
res = [sub for sub in test_list if sub[K] in check_list]

# printing result 
print("The filtered tuples : " + str(res))
# Python3 code to demonstrate working of 
# Filter Tuples by Kth element from List
# Using list comprehension

# initializing list
test_list = [("GFg", 5, 9), ("is", 4, 3), ("best", 10, 29)]

# printing original list
print("The original list is : " + str(test_list))

# initializing check_list
check_list = [4, 2, 8, 10]

# initializing K 
K = 1

# checking for presence on Kth element in list 
# one liner 
res = [sub for sub in test_list if sub[K] in check_list]

# printing result 
print("The filtered tuples : " + str(res))


'''
Python  Closest Pair to Kth index element in Tuple
'''

test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)] 
tup = (17, 23)

# Python3 code to demonstrate working of 
# Closest Pair to Kth index element in Tuple
# Using enumerate() + loop

# initializing list
test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]

# printing original list
print("The original list is : " + str(test_list))

# initializing tuple
tup = (17, 23)

# initializing K 
K = 1

# Closest Pair to Kth index element in Tuple
# Using enumerate() + loop
min_dif, res = 999999999, None
for idx, val in enumerate(test_list):
    dif = abs(tup[K - 1] - val[K - 1])
    if dif < min_dif:  # corrected here
        min_dif, res = dif, idx

# printing result 
print("The nearest tuple to Kth index element is : " + str(test_list[res]))



# Python3 code to demonstrate working of 
# Closest Pair to Kth index element in Tuple
# Using min() + lambda

# initializing list
test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]

# printing original list
print("The original list is : " + str(test_list))

# initializing tuple
tup = (17, 23)

# initializing K 
K = 1

# Closest Pair to Kth index element in Tuple
# Using min() + lambda
res = min(range(len(test_list)), key = lambda sub: abs(test_list[sub][K - 1] - tup[K - 1]))

# printing result 
print("The nearest tuple to Kth index element is : " + str(res)) 


# Python3 code to demonstrate working of 
# Tuple List intersection [ Order irrespective ]
# Using sorted() + set() + & operator + list comprehension

# initializing lists
test_list1 = [(3, 4), (5, 6), (9, 10), (4, 5)]
test_list2 = [(5, 4), (3, 4), (6, 5), (9, 11)]

# printing original list
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Using sorted() + set() + & operator + list comprehension
# Using & operator to intersect, sorting before performing intersection
res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])

# printing result 

print("List after intersection : " + str(res)) 



# Python3 code to demonstrate working of
# Unique Tuple Frequency [ Order Irrespective ]
# Using tuple() + list comprehension + sorted() + len()

# initializing lists
test_list = [(3, 4), (1, 2), (4, 3), (5, 6)]

# printing original list
print("The original list is : " + str(test_list))

# Using tuple() + list comprehension + sorted() + len()
# Size computed after conversion to set
res = len(list(set(tuple(sorted(sub)) for sub in test_list)))

# printing result
print("Unique tuples Frequency : " + str(res))

# Python3 code to demonstrate working of
# Unique Tuple Frequency [ Order Irrespective ]
# Using map() + sorted() + tuple() + set() + len()

# initializing lists
test_list = [(3, 4), (1, 2), (4, 3), (5, 6)]

# printing original list
print("The original list is : " + str(test_list))

# Using map() + sorted() + tuple() + set() + len()
# inner map used to perform sort and outer sort to
# convert again in tuple format
res = len(list(set(map(tuple, map(sorted, test_list)))))

# printing result
print("Unique tuples Frequency : " + str(res))






      








