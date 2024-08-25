# python program to demonstrate
# unique combination of two lists
# using zip() and permutation of itertools

# import itertools package
import itertools
from itertools import permutations 

# initialize lists
list_1 = ["a", "b", "c","d"]
list_2 = [1,4,9]

# create empty list to store the
# combinations
unique_combinations = []

# Getting all permutations of list_1 
# with length of list_2
permut = itertools.permutations(list_1, len(list_2))

# zip() is called to pair each permutation
# and shorter list element into combination
for comb in permut:
	
	zipped = zip(comb, list_2)
	#print(list(zipped))
	
	unique_combinations.append(list(zipped))

# printing unique_combination list 
#print(unique_combinations)


# python program to demonstrate
# unique combination of two lists
# using zip() and product() of itertools

# import itertools package
import itertools
from itertools import product 

# initialize lists
list_1 = ["b","c","d"]
list_2 = [1,4,9]

# create empty list to store the combinations
unique_combinations = []

# Extract Combination Mapping in two lists 
# using zip() + product() 

unique_combinations = list(list(zip(list_1, element))for element in product(list_2, repeat = len(list_1)))

# printing unique_combination list 
#print(unique_combinations)



def remove_items(test_list, item): 

	# using list comprehension to perform the task 
	res = [i for i in test_list if i != item] 
	return res 

# driver code 
if __name__ == "__main__": 
	test_list = [1, 3, 4, 6, 5, 1] 
	# the item which is to be removed 
	item = 1
	print("The original list is : " + str(test_list)) 

	# calling the function remove_items() 
	res = remove_items(test_list, item) 

	# printing result 
	print("The list after performing the remove operation is : " + str(res)) 




# Python3 code to demonstrate working of 
# Remove Consecutive K element records
# Using zip() + list comprehension

# initializing list
test_list = [(4, 5, 6, 3), (5, 6, 6, 9), (1, 3, 5, 6), (6, 6, 7, 8)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K 
K = 6

# Remove Consecutive K element records
# Using zip() + list comprehension
res = [idx for idx in test_list if (K, K) not in zip(idx, idx[1:])]

# printing result 
print("The records after removal : " + str(res)) 




# Python3 code to demonstrate working of 
# Remove Consecutive K element records
# Using any() + list comprehension

# initializing list
test_list = [(4, 5, 6, 3), (5, 6, 6, 9), (1, 3, 5, 6), (6, 6, 7, 8)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K 
K = 6

# Remove Consecutive K element records
# Using any() + list comprehension
res = [idx for idx in test_list if not any(idx[j] == K and idx[j + 1] == K for j in range(len(idx) - 1))]

# printing result 
print("The records after removal : " + str(res)) 



# Python3 code to demonstrate 
# Replace index elements with elements in Other List
# using list comprehension

# Initializing lists
test_list1 = ['Gfg', 'is', 'best']
test_list2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Replace index elements with elements in Other List
# using list comprehension
res = [test_list1[idx] for idx in test_list2]
			
# printing result 
print ("The lists after index elements replacements is : " + str(res))



# Python3 code to demonstrate 
# Replace index elements with elements in Other List
# using map() + lambda

# Initializing lists
test_list1 = ['Gfg', 'is', 'best']
test_list2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Replace index elements with elements in Other List
# using map() + lambda
res = list(map(lambda idx: test_list1[idx], test_list2))
			
# printing result 
print ("The lists after index elements replacements is : " + str(res))



dates = [[('2024','jan','21')],[('2024','jan','20')],[('2023','jan','20')],[('2024','feb','20')]]

nested_dict = {}
for i in dates:
        for year, month,date in i:
            if year  not in nested_dict:
                nested_dict[year]= {}
                
            if month not in  nested_dict[year]:
                
                

                nested_dict[year][month] = {'month' : month,'date' :[date]}
            else:
                nested_dict[year][month]['date'].append(date)

print(nested_dict)


# Python3 code to demonstrate 
# Swap elements in String list
# using replace() + join() + split()

# Initializing list
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

# printing original lists
print("The original list is : " + str(test_list))

# Swap elements in String list
# using replace() + join() + split()
res = ", ".join(test_list)
print(res)
res = res.replace("G", "_").replace("e", "G").replace("_", "e").split(', ')

# printing result 
print ("List after performing character swaps : " + str(res))




