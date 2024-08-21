# question:
# write a python program to print a duplicate of integer in alist

def print_duplicate(lst):
    ls = []
    for i in lst:
            if i not in ls:
                  ls.append(i)
            else:
                  print(i,end=',')

list1 = [10, 20, 30, 20, 20, 30, 40,50, -20, 60, 60, -20, -20]
print_duplicate(list1)


from collections import Counter

l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
d = Counter(l1)

new_list = list([item for item in d if d[item]>1])
print(new_list)



# program to print duplicate numbers in a given list
# provided input
list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

new = [] # defining output list

# condition for reviewing every
# element of given input list
for a in list:

	# checking the occurrence of elements
	n = list.count(a)

	# if the occurrence is more than
	# one we add it to the output list
	if n > 1:

		if new.count(a) == 0: # condition to check

			new.append(a)

print(new)

# This code is contributed by Himanshu Khune


# question 
# remove empty list from list:

def remove_empty_list(lst):
       lst = [i for i in lst if i]
       return lst

lst= [[],[1,2,3],[1,2,3],[','],[4,5]]

print(remove_empty_list(lst))



def remove_empty_lst(lst):
       lst = [i for i in lst if len(i)>=1]
       return lst

lst= [[],[1,2,3],[1,2,3],[','],[4,5]]

print(remove_empty_lst(lst))


# Python – Convert List to List of dictionaries

def convert_list_of_dict(lst):

       d =  [{'name': lst[i],'number':lst[i+1]}for i in range(0,len(lst),2)]
       return d

     
print(convert_list_of_dict(["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]))



# Question


#Python – List product excluding duplicates

def remove_duplicate_prod(lst):
       def prod(l):
              res =1
              for i in l:
                     res*=i
              return res
       l =[]
       for i in list:
              if i not in l:
                     l.append(i)
       print(prod(l))

list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
remove_duplicate_prod(list)


#Python – Extract elements with Frequency greater than K


def frequecy_ele(lst,k):
       newl=[]
       for i in lst:
              g = lst.count(i)
              if g == k   and   i not in newl:
                     newl.append(i)
                   
 
       return newl

test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
print(frequecy_ele(test_list,3 ))



test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
k = 2
unique_elems = []
freq_dict = {}
output = []

# printing string
print("The original list : " + str(test_list))

for i in test_list:
	# Append in the unique element list
	if i not in unique_elems:
		unique_elems.append(i)
		freq_dict[i] = 1
	else:
		# increment the counter if element is duplicate
		freq_dict[i] += 1

	# Add in the output list only once
	if freq_dict[i] == k +1 :
		output.append(i)
              
print('The required elements : ', str(output))
