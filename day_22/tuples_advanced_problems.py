'''
remove tuple length of k
test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
'''
k = 2
test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
filter_tup = [ i for i in test_list if len(i) > k or len(i) < k ]
print(filter_tup)


# Python3 code to demonstrate working of 
# Remove Tuples of Length K
# Using filter() + lambda + len() 

# initializing list
test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

# printing original list
print("The original list : " + str(test_list))

# initializing K 
K = 1

# filter() filters non K length values and returns result
res = list(filter(lambda x : len(x) != K, test_list))

# printing result 
print("Filtered list : " + str(res))




'''
remove none values in list of tupeles
'''
test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )] 
filter_tuples = [ i for i in test_list if  any(i for ii in i if ii!=None)]
print(filter_tuples)


'''
Python program to sort a list of tuples by second Item
 [('for', 24), ('Geeks', 8), ('Geeks', 30)]

'''


# Python program to sort a list of tuples by the second Item

# Function to sort the list of tuples by its second item


def Sort_Tuple(tup):
	# getting length of list of tuples
    for i in range(0,len(tup)):
          for j in range(0,len(tup)-i-1):
               if tup[j][1] > tup[j+1][1]:
                    tup[j],tup[j+1] = tup[j+1],tup[j]
    return tup

# Driver Code
tup = [('for', 24), ('is', 10), ('Geeks', 28),
	('Geeksforgeeks', 5), ('portal', 20), ('a', 15)]

print(Sort_Tuple(tup))



# Python3 code to demonstrate working of
# Records with Value at K index
# Using loop

# initialize list 
test_list = [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]

# printing original list
print("The original list is : " + str(test_list))

# initialize ele 
ele = 3

# initialize K 
K = 1

# Records with Value at K index
# Using loop
# using y for K = 1 
res = []
for x, y, z in test_list:
	if y == ele:
		res.append((x, y, z))

# printing result
print("The tuples of element at Kth position : " + str(res))



'''
Python program to find tuples which have all elements divisible by K from a list of tuples
'''
test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
k = 6 
test = [tuple(i for i in val if i %6==0)for val in test_list]
print(test)



'''
Input : test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)] 
Output : [(4, 5, 9)] 
Python program to find Tuples with positive elements in List of tuples

'''

test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)]
positive_tup = [val for val in test_list if  all( i>0 for i in val  )]
print(positive_tup)


# Python3 code to demonstrate working of
# Remove duplicate lists in tuples(Preserving Order)
# Using OrderedDict() + tuple()
