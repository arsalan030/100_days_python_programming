from collections import defaultdict

# initializing list
test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]

# printing original list
print("The original list is : " + str(test_list))

# Join Tuples if similar initial element
# Using defaultdict() + loop
mapp = defaultdict(list)
for key, val in test_list:
	mapp[key].append(val)
res = [(key, *val) for key, val in mapp.items()]

# printing result
print("The extracted elements : " + str(res))

'''
Python  All pair combinations of 2 tuples
'''
'''
Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8) 
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)] 

'''
lst = []
test_tuple1 = (7, 2)
test_tuple2 = (7, 8)

test_tup = [test_tuple1,test_tuple2]
for vaal1 in test_tuple1:
     for vaal2 in test_tuple2:
          lst.append((vaal1,vaal2))
          lst.append((vaal2,vaal1))
print(lst)



# Python3 code to demonstrate working of 
# Remove None Tuples from List
# Using filter() + lambda + all()

# initializing list
test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]

# printing original list
print("The original list is : " + str(test_list))

# filter() + lambda to drive logic of discarding tuples
res = list(filter(lambda sub : not all(ele == None for ele in sub), test_list))

# printing result 
print("Removed None Tuples : " + str(res))

''''
Python program to sort a list of tuples by second Item
'''

