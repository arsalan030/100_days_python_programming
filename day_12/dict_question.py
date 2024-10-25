'''
Section A: Basic Operations on Dictionaries
    1. Python Program to Sort Dictionaries by Key or Value
        ◦ Write a Python program to sort a dictionary by its keys or values.
       Input:
       python
       Copy code
       d = {'banana': 3, 'apple': 2, 'orange': 1}
       Expected Output (Sorted by Key):
       python
       Copy code
       {'apple': 2, 'banana': 3, 'orange': 1}
       '''

d = {'apple': 2, 'banana': 3, 'orange': 1}
 
 #by key
sorted_dict = dict(sorted(d.items(),key=lambda d : d[0]))
print(sorted_dict)

sorted_dict = dict(sorted(d.items(),key=lambda d : d[1]))
print(sorted_dict)


'''
    2. Handling Missing Keys in Python Dictionaries
        ◦ Write a program to handle missing keys in a dictionary using get().
       Input:
       python
       Copy code
       d = {'name': 'John', 'age': 25}
x
       Expected Output:
       python
       Copy code
'''

d = {'name': 'John', 'age': 25}
f = d.get('arsalan','key is not found')
print(f)

from collections import defaultdict
dd = defaultdict(list)
dd['arsalan'].append('ahmed')
print(dd)



''''
    3. Find Sum of All Items in a Dictionary
        ◦ Write a program to find the sum of all values in a dictionary.
       Input:
       python
       Copy code
       d = {'a': 100, 'b': 200, 'c': 300}
       Expected Output:
       python
       Copy code
       600
'''

d = {'a': 100, 'b': 200, 'c': 300}
s= 0
for i in d.values():
    s+=i
print(s)

d = sum((v for v in d.values()))
print(d)

