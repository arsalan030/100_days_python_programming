'''
a set contains name with begins with a or b writea program to seprate out the names in to two sets one containning names witha a an
other conatininng names with b
'''

setA= {'arsalan','ahmed','arif','ahsan','ali','bilal','bila','basics','basjif','bazizzz','bqaiii','ahsan'}
setA.remove('ali')

print(setA)

seta = set()
setb = set()
for name  in setA:
    if name.startswith('a'):
        seta.add(name)
    else:

        setb.add(name)

print(seta,setb)

import random

'''
write a program to generate random random number in set 
'''
import random

random_set = {random.randint(11,1100)for i in range(10)}
print(random_set)

max = 0
for i in  random_set:
    if i > max:
        max = i
    
print(max,random_set)


# find three common element in  three list in set
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

arr1 = set(ar1)
arr2 = set(ar2)
arr3 = set(ar3)


set1 = arr1 .intersection(arr2)
result = set1.intersection(arr3)
print(set1)