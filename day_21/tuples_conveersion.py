test = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
test = list(sorted(test,key= lambda d:d[1]))
print(test)


'''
Input : test_list = [(3, 4, 6, 723), (1, 2), (134, 234, 34)] 
Output : [(1, 2), (3, 4, 6, 723), (134, 234, 34)] 
Explanation : 2 < 6 < 8, sorted by increasing total digits.
'''

test_list = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]
# Python3 code to demonstrate working of 
# Sort Tuples by Total digits
# Using sort() + len() + sum()

 
def count_digs(tup):
     
    # gets total digits in tuples
    return sum([len(str(ele)) for ele in tup ])


test_list.sort(key = count_digs)
print(test_list)

# initializing list




'''
sum of tuple elements
'''

tup = (7, 8, 9, 1, 10, 7)
summ = sum(i for i in tup)
print(summ)

'''
multuiply adjacent element

'''
test_tup = (1, 5, 7, 8, 10) 

test = (i*k for i,k in zip(test_tup[0:],test_tup[1:]))
print(tuple(test))


test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
new_list = [test_list[0]]

for i in test_list:
     if i[0] == new_list[-1][0]:
          new_list[-1]+=(i[1],) 
     else :
          new_list.append(i) 
print(new_list)


'''
print all paiirs of tuple

'''
test_tuple1 = (7, 2)
test_tuple2 = (7, 8) 

all_pairs = [[(a,b),(b,a)]for a in test_tuple1 for b in test_tuple2]
print(*all_pairs)



