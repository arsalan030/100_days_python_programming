'''
find maximum element and minumn kth element from tuple

Input : test_tup = (3, 7, 1, 18, 9), k = 2 
Output : (3, 1, 9, 18)
'''

# Python3 code to demonstrate working of 
# Maximum and Minimum K elements in Tuple
# Using sorted() + loop

# initializing tuple
test_tup = (5, 20, 3, 7, 6, 8)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# initializing K 
K = 2

# Maximum and Minimum K elements in Tuple
# Using sorted() + loop

res = []
test_tup = list(sorted(test_tup))

for idx, val in enumerate(test_tup):
	if idx < K or idx >= len(test_tup) - K:
		res.append(val)
res = tuple(res)

# printing result 
print("The extracted values : " + str(res)) 







def max_k_elements(tup, k):
    max_elements = [-float('inf')] * k
    for elem in tup:
        for i in range(k):
            if elem > max_elements[i]:
                max_elements = max_elements[:i] + [elem] + max_elements[i:-1]
                break
    return max_elements

def min_k_elements(tup, k):
    min_elements = [float('inf')] * k
    for elem in tup:
        for i in range(k):
            if elem < min_elements[i]:
                min_elements = min_elements[:i] + [elem] + min_elements[i:-1]
                break
    return min_elements

# Example usage:
tup = (7, 2, 5, 10, 3, 8)
k = 2
print("Max K elements:", max_k_elements(tup, k))
print("Min K elements:", min_k_elements(tup, k))

'''
Python  Modulo of tuple elements
'''

# Python3 code to demonstrate working of
# Tuple modulo
# using zip() + generator expression

# Initialize tuples
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

# Printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Tuple modulo
# using zip() + generator expression
res = tuple(ele1 % ele2 for ele1, ele2 in zip(test_tup1, test_tup2))

# Printing result
print("The modulus tuple : " + str(res))
''

        

        



    
