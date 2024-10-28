'''
Input : test_dict = {‘gfg’ : {‘x’ : 5, ‘y’ : 6, ‘z’: 3}, ‘best’ : {‘x’ : 8, ‘y’ : 3, ‘z’: 5}} Output : [(‘x’, (5, 8)), (‘y’, (6, 3)), (‘z’, (3, 5))] Input : test_dict = {‘gfg’ : {‘x’ : 5, ‘y’ : 6, ‘z’: 3}} 
Output : [(‘x’, (5, )), (‘y’, (6, )), (‘z’, (3, ))]
'''

d = {'is': {'y': 4, 'x': 1}, 'gfg': {'y': 6, 'x': 5}, 'best': {'y': 3, 'x': 8}}

def find_mapped_tupel(d):
      n_dict = d.values()
      mapped_list= []
      val_list = []
      for val in n_dict:
             val_list.append(list(val.values()))
      key_list =  val.keys()
      for idx ,k in enumerate(key_list):
                    a =tuple()
                    
                    for v in val_list:
                           a+=(v[idx],)
                        
                    mapped_list.append((k,a))
      print(mapped_list)
                    
             
      #mapped_tuple = [(k,tuple([v[indx]for v in val_list]))for indx,k  in enumerate(key_list)]
      #print(mapped_tuple)

d = {'is': {'y': 4, 'x': 1}, 'gfg': {'y': 6, 'x': 5}, 'best': {'y': 3, 'x': 8}}

print(find_mapped_tupel(d))

# Convert Nested dictionary to Mapped Tuple
# Using list comprehension + generator expression
res = [(key, tuple(sub[key] for sub in d.values()))  for key in d['gfg']]
print(res)


"Ways to convert string to dictionary"

str = " Jan = January; Feb = February; Mar = March"


d = dict(i.split('=')for i in str.split(";"))
print(d)


# Python3 code to demonstrate working of 
# Convert dictionary to K Keys dictionaries
# Using loop

# initializing dictionary
test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'geeks' : 5, 'CS' : 6}

# printing original dictionary
print("The original dictionary is : " ,test_dict)

# initializing K 
K = 2

res = []
count = 0
flag = 0
indict = dict()
for key in test_dict:
	indict[key] = test_dict[key]	 
	count += 1
	
	# checking for K size and avoiding empty dict using flag
	if count % K == 0 and flag:
		res.append(indict)
		
		# reinitializing dictionary
		indict = dict()
		count = 0
	flag = 1
	

# printing result 
print("The converted list : " , res)



       








      


             
             
