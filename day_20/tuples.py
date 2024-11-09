'''
Python – Row-wise element Addition in Tuple Matrix
Input : test_list = [[(‘Gfg’, 3)], [(‘best’, 1)]] cus_eles = [1, 2] 
Output : [[(‘Gfg’, 3, 1)], [(‘best’, 1, 2)]] 
'''
test_list = [[('Gfg', 3)], [('best' ,1)]] 
cus_eles = [1, 2] 


row_wise_elemnt = [[i+ (cus_eles[indx],)]for indx,val in enumerate(test_list) for i in val]

print(row_wise_elemnt)





test_tup = (1, 5, 7, 8, 10) 

# printing original tuple 
print("The original tuple : " + str(test_tup)) 

# Adjacent element multiplication 
# using zip() + generator expression + tuple 
res = tuple(i * j for i, j in zip(test_tup, test_tup[1:])) 

# printing result 
print("Resultant tuple after multiplication : " + str(res)) 

'''
Python  Join Tuples if similar initial element
'''
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
lst = [test_list[0]]
for k in test_list[1:]:
    if lst[-1][0] ==  k[0]:
        print(k[-1:])
        lst[-1] +=k[1:]
    else:
        lst.append(k)

print(lst)

# Python3 code to demonstrate working of
# Join Tuples if similar initial element
# Using defaultdict() + loop
