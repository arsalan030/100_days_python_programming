# write a program to sort the dict key or vaalue

import operator
d = {'zil':4,'wheel':5,'gas':10}

sorted_dict = sorted(d.items(),key=lambda d : d[0])
print(sorted_dict)
print(sorted(d.items(),key= operator.itemgetter(1)))

mykeys  =  list(d.keys())
mykeys.sort()
d  = {i:d[i] for i in mykeys}
print(d)

# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict

d = {'ravi': 10, 'rajnish': 9, 'abc': 15}
d1 = OrderedDict(sorted(d.items()))
print(d1)

sorted_items = sorted(d.items() , key=lambda kv: (kv[1], kv[0]))

print(sorted_items)

d1 =  {k:v for k,v in sorted(d.items(),key=lambda d :d[1] ,reverse= True)}
print(d1)




# Python3 code to demonstrate working of 
# Sort Dictionary key and values List
# Using lambda function with sorted()
 
# initializing dictionary
test_dict = {'gfg': [7, 6, 3], 
             'is': [2, 10, 3], 
             'best': [19, 4]}
 

 
# Sort Dictionary key and values List
# Using lambda function with sorted()
res = dict(sorted(test_dict.items(), key=lambda x: x[0]))

print(res)
 
for key in res:
    res[key] = sorted(res[key])
 
# printing result 
print("The sorted dictionary: " ,res)

places = {("19.07'53.2", "72.54'51.0"):"Mumbai", ("28.33'34.1", "77.06'16.6"):"Delhi"}
lat = []
long = []
plc = []
for i in places:
    
    lat.append(i[0])
    long.append(i[1])
    plc.append(places[i[0], i[1]])
 
print(lat)
print(long)
print(plc)

import functools

dic = {'a': 100, 'b': 200, 'c': 300}

sum_dic = functools.reduce(lambda a,k: a +dic[k], dic, 1)

print("Sum :", sum_dic)
