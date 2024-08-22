# today we solve some medium leve list questsion
# question
# Given a list of lists. The task is to extract a random element from it.

# Python3 code to demonstrate working of
# Random Matrix Element
# Using chain.from_iterables() + random.choice()
from itertools import chain
import random

# Initializing list
test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

# Printing original list
print("The original list is : " + str(test_list))

# choice() for random number, from_iterables for flattening
res = random.choice(list(chain.from_iterable(test_list)))

# Printing result
print("Random number from Matrix : " + str(res))


# same question

# Python3 code to demonstrate working of
# Random Matrix Element
# Using random.choice() [if row number given]
import random

# initializing list
test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

# printing original list
print("The original list is : " + str(test_list))

# initializing Row number
r_no = [0, 1, 2]

# choice() for random number, from_iterables for flattening
res = random.choice(test_list[random.choice(r_no)])

# printing result
print("Random number from Matrix Row : " + str(res))

test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

new_l = []+test_list[0]+test_list[1]+test_list[2]
print(random.choice(new_l))

# Python – Reverse Row sort in Lists of List

# Python3 code to demonstrate
# Reverse Row sort in Lists of List
# using loop

# initializing list
test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]

# printing original list
print("The original list is : " + str(test_list))

# Reverse Row sort in Lists of List
# using loop
for ele in test_list:
	ele.sort(reverse=True)

# printing result
print("The reverse sorted Matrix is : " + str(test_list))



# Python3 code to demonstrate
# Reverse Row sort in Lists of List
# using list comprehension + sorted()

# initializing list
test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]

# printing original list
print("The original list is : " + str(test_list))

# Reverse Row sort in Lists of List
# using list comprehension + sorted()
res = [sorted(sub, reverse=True) for sub in test_list]

# printing result
print("The reverse sorted Matrix is : " + str(res))


# Python3 code to demonstrate 
# Pair elements with Rear element in Matrix Row
# using list comprehension

# Initializing list
test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]

# printing original list
print("The original list is : " + str(test_list))

# Pair elements with Rear element in Matrix Row
# using list comprehension
res = []
for sub in test_list:
	res.append([[ele, sub[-1]] for ele in sub[:-1]])
	
# printing result 
print ("The list after pairing is : " + str(res))

# Python3 code to demonstrate 
# Pair elements with Rear element in Matrix Row
# using product() + loop
from itertools import product

# Initializing list
test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]

# printing original list
print("The original list is : " + str(test_list))

# Pair elements with Rear element in Matrix Row
# using product() + loop
res = []

for idx in test_list:
	res.append(list(product(idx[:-1], [idx[-1]])))
	
# printing result 
print ("The list after pairing is : " + str(res))

# Python3 code to demonstrate 
# Pair elements with Rear element in Matrix Row
# using list comprehension with tuple packing and unpacking

# Initializing list
test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]

# Printing original list
print("The original list is : " + str(test_list))

# Pair elements with Rear element in Matrix Row using list comprehension with tuple packing and unpacking
res = [[(ele, sub[-1]) for ele in sub[:-1]] for sub in test_list]

# Printing result 
print("The list after pairing is : " + str(res))



# Python3 code to demonstrate 
# Test if List contains elements in Range
# using loop

# Initializing loop 
test_list = [4, 5, 6, 7, 3, 9]

# printing original list 
print("The original list is : " + str(test_list))

# Initialization of range 
i, j = 3, 10

# Test if List contains elements in Range
# using loop
res = True
for ele in test_list:
	if ele < i or ele >= j :
		res = False
		break

# printing result 
print ("Does list contain all elements in range : " + str(res))




# Python3 code to demonstrate 
# Test if List contains elements in Range
# using all()

# Initializing loop 
test_list = [4, 5, 6, 7, 3, 9]

# printing original list 
print("The original list is : " + str(test_list))

# Initialization of range 
i, j = 3, 10

# Test if List contains elements in Range
# using all()
res = all(ele >= i and ele < j for ele in test_list) 

# printing result 
print ("Does list contain all elements in range : " + str(res))


lst = [1 , 2 ,2 ,3 ,4 ,5]


# find the strongest negibour in lst
res = [max([lst[i],lst[i-1]]) for i in range(1,len(lst))]
print(res)


# python program print all possiable combinations

i=1
while i<=3:
	j=1
	while j<=3:
		k=1
		while k<=3:
			if i!=j and j!=k and  i!=k:
				print(i,j,k)
				
			k+=1
		j+=1
	i+=1
				
			
	


	
				  
                  
		
			

	
	