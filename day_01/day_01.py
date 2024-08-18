# Question no1 

# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
    
    newList[0], newList[-1] = newList[-1], newList[0]

    return newList
    
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
    size = len(newList)
    
    # Swapping 
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    
    return newList
    
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))



# Questsion no 2
# swap the elements of given psoitions

def swapt_postions(newlist, pos1,pos2):

    newList[1],newList[pos2] = newList[pos2],newList[pos1]
    return newList

print(swapt_postions(newList,1,3))


# Question no 3
# swap the elements 
# Python3 code to demonstrate 
# Swap elements in String list
# using replace() + list comprehension

# Initializing list
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

# printing original lists
print("The original list is : " + str(test_list))

# Swap elements in String list
# using replace() + list comprehension
res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]

# printing result 
print ("List after performing character swaps : " + str(res))

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
res = res.replace("G", "_").replace("e", "G").replace("_", "e").split(', ')

# printing result 
print ("List after performing character swaps : " + str(res))



# question no 4
# Initializing list
test_list = [1, 6, 3, 5, 3, 4]

result = any(item in test_list for item in test_list)
print("Does string contain any list element : " +str(bool(result)))



# Initializing list
test_list = [1, 6, 3, 5, 3, 4]

# Checking if 4 exists in list
for i in test_list:
    if(i == 4):
        print("Element Exists")



