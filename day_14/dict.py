'''
    8. Find Common Elements in Three Sorted Arrays by Dictionary Intersection
        ◦ Use dictionary intersection to find common elements in three sorted arrays.
       Input:
       python
       Copy code
       arr1 = [1, 2, 3, 4, 5]
       arr2 = [1, 2, 5, 7, 9]
       arr3 = [1, 3, 4, 5, 8]
       Expected Output:
       python
       Copy code
       [1, 5]
'''



from collections import Counter
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 2, 5, 8]

commomn = [i  for i in arr1 if i in arr2 and i in arr3 ] 

print(commomn)


'''
    10. Remove Duplicate Values Across Dictionary Values
        ◦ Write a Python program to remove duplicate values across dictionary keys.
       Input:
       python
       Copy code
       d = {'A': [1, 2, 2, 3], 'B': [2, 3, 4, 4], 'C': [1, 5, 6]}
       Expected Output:
       python
       Copy code
       {'A': [1, 2, 3], 'B': [3, 4], 'C': [5, 6]}
'''

d = {'A': [1, 2, 2, 3], 'B': [2, 3, 4, 4], 'C': [1, 5, 6]}

def unieq__values(d):
    seen = set()
    
    for k,v in d.items():
        unieq__value = []
        for j in v:
            if j not in seen:
                unieq__value.append(j)
                seen.add(j)
        d[k]=unieq__value
    return d
print(unieq__values(d))


# Python3 code to demonstrate working of
# Remove duplicate values across Dictionary Values
# Using Counter() + list comprehension




            

 





















