str = ["geeksforgeeks" , 'best','geeks','for','geeks']
prefix  = 'geeks'
new = []
for  i in str:
    if i.startswith(prefix):
        new.append([i])
    else:
        new[-1].append(i)
print(new)

test_list = ['G','F','H','I','J','K']
newlist = [ '*' if i!= 'G' else 'G'for i in test_list]
print(newlist)


test_list = ['gfgBest' , 'forGeeks','andComputerScienceStudent']

newlist = []
for i in test_list:
    res = ""
    
    for item in range(len(i)):
       
        if i[item].islower():

            res += i[item]
        else:
            
            res+=" " + i[item]
           
    newlist.append(res)

print(newlist)


# Python3 code to demonstrate working of 
# Add Space between Potential Words
# Using loop + join()

# initializing list
test_list = ["gfgBest", "forGeeks", "andComputerScience"]

# printing original list


res = []

# loop to iterate all strings 
for ele in test_list:
	temp = [[]]
	for char in ele:
		
		# checking for upper case character
		if char.isupper():
			temp.append([])
			
		# appending character at latest list
		temp[-1].append(char)
	
	# joining lists after adding space
	res.append(' '.join(''.join(ele) for ele in temp))

# printing result 
print(res)


test_list1 = ['Gfg', 'is', 'not', 'best', 'and', 'not', 'CS']
test_list2 = ['Its ok', 'all ok', 'wrong', 'looks ok', 'ok', 'wrong', 'thats ok']
new = []
new = [i for  i,l in zip(test_list1,test_list2) if  'ok' in l]
    
print(new)
          


# Python3 code to demonstrate working of
# Extract elements filtered by substring

# initializing list
test_list1 = ["Gfg", "is", "not", "best", "and",
			"not", "for", "CS"]
test_list2 = ["Its ok", "all ok", "wrong", "looks ok",
						"ok", "wrong", "ok", "thats ok"]

# printing original lists
print("The original list 1 is : " ,test_list1)
print("The original list 2 is : " ,test_list2)

# initializing substr
sub_str = "ok"

res = []
for i in range(0, len(test_list2)):
	if test_list2[i].find(sub_str) != -1:
		res.append(test_list1[i])


# printing result
print("The extracted list : " ,res )

         
    


