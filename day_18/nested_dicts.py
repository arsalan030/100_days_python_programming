'''
The original dictionary is : {'a': {'b': {'c': {}}}, 'd': {'e': {}}, 'f': {'g': {'h': {}}}}
The inverted dictionary : {'c': {'b': {'a': {}}}, 'e': {'d': {}}, 'h': {'g': {'f': {}}}}
'''
orignal_dict = {'a': {'b': {'c': {}}}, 'd': {'e': {}}, 'f': {'g': {'h': {}}}}
indict= {}
for k,v in orignal_dict.items():
      temp2 =dict()
      for kk,vv in v.items():
            temp1 = dict()
            if vv.items():
                    for kkk,vvv in vv.items():
                        temp1[k]={}
                        if kk not in  temp2:
                            temp2[kk]=temp1
                            if k not in indict:
                                    indict[kkk]=temp2                     
            else:
                 temp1[kk]=vv
                 if kk not in indict:
                        indict[k]=temp1
                        
                        
                                
print(indict)




# Python3 code to demonstrate working of 
# Inversion in nested dictionary
# Using loop + recursion

# utility function to get all paths till end 
def extract_path(test_dict, path_way):
	if not test_dict:
		return [path_way]
	temp = []
	for key in test_dict:
		temp.extend(extract_path(test_dict[key], path_way + [key]))
	return temp

# function to compute inversion
def hlper_fnc(test_dict):
	all_paths = extract_path(test_dict, [])
	res = {}
	for path in all_paths:
		front = res
		for ele in path[::-1]:
			if ele not in front :
				front[ele] = {}
			front = front[ele]
	return res

# initializing dictionary
test_dict = {"a" : {"b" : {"c" : {}}},
			"d" : {"e" : {}},
			"f" : {"g" : {"h" : {}}}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# calling helper function for task 
res = hlper_fnc(test_dict)

# printing result 
print("The inverted dictionary : " + str(res)) 




original_dict = {'a': {'b': {'c': {}}}, 'd': {'e': {}}, 'f': {'g': {'h': {}}}}
indict = {}

for k, v in original_dict.items():
    for kk, vv in v.items():
        indict[kk] = {k: vv if vv else {}}

print(indict)


original_dict = {'a': {'b': {'c': {}}}, 'd': {'e': {}}, 'f': {'g': {'h': {}}}}

inverted_dict = {}

for k, v in original_dict.items():
    for kk, vv in v.items():
        if vv.items():
                
            for kkk in vv:
                inverted_dict[kkk] = {kk: {k: {}}}  # Invert the keys in a single assignment
        else:
              inverted_dict[kk] = {k:{}}


print("The inverted dictionary:", inverted_dict)




