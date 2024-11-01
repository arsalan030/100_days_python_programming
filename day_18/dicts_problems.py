'''Input : test_list = [[5, 6, 7], [8, 3, 2]] Output : {1: [5, 6, 7], 2: [8, 3,2]]'''

test_list = [[5, 6, 7], [8, 3, 2]]
d = {i : val for i ,val in enumerate(test_list,start = 1)}
print(d)
res = {idx: val for idx, val in enumerate(test_list, start = 1)}
print(res)

''''
The original dictionary is : {‘name’: [‘Jan’, ‘Feb’, ‘March’], ‘month’: [1, 2, 3]} Flattened dictionary : {1: ‘Jan’, 2: ‘Feb’, 3: ‘March’}

'''
orignal_d = {'name': ['Jan', 'Feb', 'March'],'month' : [1, 2, 3]}


val = list(orignal_d.values())
flateened_d = {k:v  for  k,v in zip(val[0],val[1])}
print(flateened_d)

test_dict = {'gfg' : {'x' : 5, 'y' : 6, 'z': 3}, 'best' : {'x' : 8, 'y': 3, 'z': 5}} 


mapped__tuple = ((k,tuple(di[k] for di in test_dict.values())) for k in test_dict['gfg'] )


print(tuple(mapped__tuple))


test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'geeks' : 5, 'CS' : 6}





dd = {}
l=[]
k=3
for ke ,v in test_dict.items():
    dd[ke]=v

    if len(dd) == k:
        l.append(dd)
        counter = 0
        dd = {}
print(l)

'''
input : test_dict = {‘Gfg’: { ‘a’ : [1, 3, 7, 8], ‘b’ : [4, 9], ‘c’ : [0, 7]}} 
Output : {‘c’: {‘Gfg’: [0, 7]}, ‘b’: {‘Gfg’: [4, 9]}, ‘a’: {‘Gfg’: [1, 3, 7, 8]}}
'''
from collections import defaultdict

test_dict = {'Gfg': {'a' : [1, 3, 7, 8], 'b' : [4, 9], 'c' : [0, 7]}}

new_dict = defaultdict(dict)
for k,v in test_dict.items():
    for kk,vv in v.items():
        f = test_dict[k][kk]
        new_dict[kk].update({k:f})
print(new_dict)

res = dict()
for key, val in test_dict.items():
	for key_in, val_in in val.items():
		if key_in not in res:
			temp = dict()
		else:
			temp = res[key_in]
		temp[key] = val_in
		res[key_in] = temp

# printing result 
print("The rearranged dictionary : " + str(res)) 


# Python3 code to demonstrate working of 
# Swapping Hierarchy in Nested Dictionaries
# Using loop + items()

# initializing dictionary
test_dict = {'Gfg': { 'a' : [1, 3], 'b' : [3, 6], 'c' : [6, 7, 8]},
			'Best': { 'a' : [7, 9], 'b' : [5, 3, 2], 'd' : [0, 1, 0]}}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Swapping Hierarchy in Nested Dictionaries
# Using loop + items()
'''
input : test_dict = {“a” : {“b” : {}}, “d” : {“e” : {}}, “f” : {“g” : {}} 
Output : {‘b’: {‘a’: {}}, ‘e’: {‘d’: {}}, ‘g’: {‘f’: {}}

'''
test_dict = {"a" : {"b" : {}}, "d" : {"e" : {}}, "f" : {"g" : {}} }

indect = {}
for k,v in test_dict.items():
      temp = dict()
      for kk,vv in v.items():
            temp= {}
            temp[k]=vv
            if kk not in indect:
                  indect[kk] = temp
                  

print(indect)


test_dict = {'Manjeet': [1, 4, 5, 6],
             'Akash': [1, 8, 9],
             'Nikhil': [10, 22, 4],
             'Akshat': [5, 11, 22]}

seen = set()

for k,v in test_dict.items():
      new_value =[]
      for vv in v:
            if vv not in seen:
                  new_value.append(vv)
                  seen.add(vv)
      test_dict[k]=new_value

            
print(test_dict)




# Python3 code to demonstrate working of
# Remove duplicate values across Dictionary Values
# Using Counter() + list comprehension
from collections import Counter

# initializing dictionary
test_dict = {'Manjeet': [1, 4, 5, 6],
			'Akash': [1, 8, 9],
			'Nikhil': [10, 22, 4],
			'Akshat': [5, 11, 22]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Remove duplicate values across Dictionary Values
# Using Counter() + list comprehension
cnt = Counter()
for idx in test_dict.values():
	cnt.update(idx)
res = {idx: [key for key in j if cnt[key] == 1]
	for idx, j in test_dict.items()}

# printing result
print("Uncommon elements records : " + str(res))

'''
Input : 
test_dict = {1 : ‘Gfg is best for geeks’} 
sub_list = [‘love’, ‘good’] ( Strings to check in values ) 
Output : {1: ‘Gfg is best for geeks’}

'''
      
test_dict = {1 : 'Gfg is best for geeks', 2 : 'Gfg is good', 3 : 'I love Gfg'}
sub_list = ['love', 'good']


d = {k:val for k ,val in test_dict.items()if  all(v not in sub_list for v in val.split(' '))}
print(d)

'''
nput : test_dict = {‘Gfg’ : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6, ‘geeks’ : ‘CS’}, K = 7 
Output : {‘Gfg’ : 3, ‘for’ : 6, ‘geeks’ : ‘CS’} 
Explanation : All values greater than K are removed. Mixed value is retained. 


'''
from collections import OrderedDict
test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'geeks' : 'CS'}
d ={}
K = 6
 
# using loop to iterate keys of dictionary
res = {key : val for key, val in test_dict.items() if not (isinstance(val, int) and (val > K))}

res =dict(reversed(test_dict.items()))
print(res)


res = dict(reversed(test_dict.items()))

print(res)

'''
Python – Dictionary with maximum count of pairs
[{“gfg”: 2, “best” : 4}, {“gfg”: 2, “is” : 3, “best” : 4, “CS” : 9}, {“gfg”: 2}]

'''
test_dict = [{"gfg": 2, "best" : 4}, {"gfg": 2, "is" : 3, "best" : 4, "CS" : 9}, {"gfg": 2}]


d = {len(k) : k for k in test_dict }
maxx  = max(list(d.keys()))
print(d[maxx],maxx)



'''
Input : test_dict = {“Gfg” : 1, “is” : 2, “Best” : 3} 
Output : [‘Gfg’, ‘is’, ‘Best’, 1, 2, 3] 

'''
test_dict = {'Gfg' : 1, 'is' : 2, 'Best' : 3}

print([k for k in  test_dict.keys()] +[k for k in  test_dict.values()] )

'''
The original dictionary is : {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
The unique values list is : [1, 2, 5, 6, 7, 8, 10, 11, 12
'''

test_dict = {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}

unieq_val  = list(set(k for kk in test_dict.values() for k in kk ))
print(unieq_val)

'''
Python – Keys associated with Values in Dictionary
nput : test_dict = {‘abc’ : [10, 30], ‘bcd’ : [30, 40, 10]} 
Output : {10: [‘abc’, ‘bcd’], 30: [‘abc’, ‘bcd’], 40: [‘bcd’]} 

'''
test_dict = {'abc' : [10, 30], 'bcd' : [30, 40, 10]}
new_dict = defaultdict(list)
{new_dict[v].append(kk)for kk ,vv in test_dict.items() for v in vv if new_dict[v] != kk}
                  

print(new_dict)




# Function to return all anagrams together
def allAnagram(input):
	
	# empty dictionary which holds subsets
	# of all anagrams together
	dict = {}

	# traverse list of strings
	for strVal in input:
		
		# sorted(iterable) method accepts any
		# iterable and returns list of items
		# in ascending order
		key = ''.join(sorted(strVal))
		
		# now check if key exist in dictionary
		# or not. If yes then simply append the
		# strVal into the list of it's corresponding
		# key. If not then map empty list onto
		# key and then start appending values
		if key in dict.keys():
			dict[key].append(strVal)
		else:
			dict[key] = []
			dict[key].append(strVal)

	# traverse dictionary and concatenate values
	# of keys together
	output = ""
	for key,value in dict.items():
		output = output + ' '.join(value) + ' '

	return output

# Driver function
if __name__ == "__main__":
	input=['cat', 'dog', 'tac', 'god', 'act']
	print (allAnagram(input))
	

# function to Check if binary representations
# of two numbers are anagram
from collections import Counter

def checkAnagram(num1,num2):

	# convert numbers into in binary
	# and remove first two characters of 
	# output string because bin function 
	# '0b' as prefix in output string
	bin1 = bin(num1)[2:]
	bin2 = bin(num2)[2:]

	# append zeros in shorter string
	zeros = abs(len(bin1)-len(bin2))
	if (len(bin1)>len(bin2)):
		bin2 = zeros * '0' + bin2
	else:
		bin1 = zeros * '0' + bin1

	# convert binary representations 
	# into dictionary
	dict1 = Counter(bin1)
	dict2 = Counter(bin2)

	# compare both dictionaries
	if dict1 == dict2:
		print('Yes')
	else:
		print('No')

# Driver program
if __name__ == "__main__":
	num1 = 10
	num2 = 12
	checkAnagram(num1,num2)
	
'''
 [{“Gfg” : [6, 7, 8], “is” : 9, “best” : 10}, {“Gfg” : [2, 0, 3], “is” : 11, “best” : 19}, {“Gfg” : [4, 6, 9], “is” : 16, “best” : 1}]



 K = “Gfg”, idx = 0 
Output : [{‘Gfg’: [2, 0, 3], ‘is’: 11, ‘best’: 19}, {‘Gfg’: [4, 6, 9], ‘is’: 16, ‘best’: 1}, {‘Gfg’: [6, 7, 8], ‘is’: 9, ‘best’: 10}] 
'''
	
test_dict =  [{'Gfg' : [6, 7, 8], 'is' : 9, 'best' : 10}, {'Gfg' : [2, 0, 3], 'is' : 11, 'best' : 19}, {'Gfg' : [4, 6, 9], 'is' : 16, 'best' : 1}]
sorted_dict = sorted(test_dict ,key= lambda d : d['Gfg'][0])

print(sorted_dict)



# Python3 code to demonstrate working of 
# Sort Nested keys by Value
# Using sorted() + generator expression + lambda
print()
 
# initializing dictionary
test_dict = {'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
             'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
             'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}}

sorted_dict = {key :dict(sorted(val.items(),key = lambda d: d[1]))for key , val  in test_dict.items()}

print(sorted_dict)



test_list = [['gfg', 'is', 'best'], ['gfg', 'is', 'for', 'geeks']]
test_dict = {'gfg' : 5, 'is' : 10, 'best' : 13, 'for' : 2, 'geeks' : 15}
result_list = [[sum(test_dict [ii] for ii in i)]for i in test_list]
print(result_list)
