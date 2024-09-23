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
lst  = [1,2,3]
t = [(i,i*i*i)for i in lst]
print(t)

# row wise elemnts add in tuple
test_list = [[('Gfg', 3)], [('best', 1)]]
s = [1, 2] 
t= [[[sub  + (s[idx],)] for  sub in val]for idx ,val in enumerate(test_list) ]

print(t)

test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
l = [test_list[0]]
for i in range(1,len(test_list)):
	
	if l[-1][0] in test_list[i]:
		l[-1]+= test_list[i][1:] 
	else:
		l += (test_list[i],)
print(l)

test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]
t = [sub for sub in test_list if not all( i== None for  i in sub )]
print(t)

# Python program to sort a list of
# tuples by the second Item using sorted() 

# Function to sort the list by second item of tuple
def Sort_Tuple(tup): 

	# reverse = None (Sorts in Ascending order) 
	# key is set to sort using second element of 
	# sublist lambda has been used 
	return(sorted(tup, key = lambda x: x[1])) 

# Driver Code 
tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)] 

# printing the sorted list of tuples
print(Sort_Tuple(tup)) 

test_list = [(3, 4, 6, 723), (1, 2), (134, 234, 34)]
t =[sorted(sub)for sub in test_list]
print(t)

test_list = [(6, 5, 8), (2, 7), (6, 5, 8), (9, ), (2, 7)] 
t= {sub : test_list.count(sub)for sub in test_list}
t= [k + (v,)for k,v in t.items()]
print(t)


# Python3 code to demonstrate working of 
# Test if tuple is distinct 
# Using loop 

# initialize tuple 
test_tup = (1, 4, 5, 6, 1, 4) 

# printing original tuple 
print("The original tuple is : " + str(test_tup)) 

# Test if tuple is distinct 
# Using loop 
res = True
temp = set() 
for ele in test_tup: 
	if ele in temp: 
		res = False
		break
	temp.add(ele) 

# printing result 
print("Is tuple distinct ? : " + str(res)) 

# Python3 code to demonstrate working of
# K Multiple Elements Tuples
# Using list comprehension + all()

# initializing list
test_list = [(6, 24, 12), (7, 9, 6), (12, 18, 21)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 6

# all() used to filter elements
res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]

# printing result
print("K Multiple elements tuples : " + str(res))





d = {'arsalan' :40, 'ali':30}


d1 = filter(lambda k : d[k]>= 40,d)
print(list(d1))

l = ['madam','racecar','Level','rafdar','deiffied','civccic','rotor','noon','refer','wow']

f = filter(lambda n : n.replace(" ","").lower()==n[::-1].lower(),l)
print(list(f))
	
	
y = ['abba','noon','xyzxyz','abcdabcd','123123','aabb','meme','gogogo','redred','poopo']

g = filter(lambda n : n[:len(n)//2]==n[-len(n)//2:] ,y)
h = filter(lambda n : len(n)<=5 ,y)
print(list(g))
print(list(h))

employees = {
    1: {
        "name": "Alice Johnson",
        "age": 29,
        "department": "Finance",
        "employee_id": "EMP001"
    },
    2: {
        "name": "Bob Smith",
        "age": 35,
        "department": "Marketing",
        "employee_id": "EMP002"
    },
    3: {
        "name": "Carol Williams",
        "age": 41,
        "department": "IT",
        "employee_id": "EMP003"
    },
    4: {
        "name": "David Brown",
        "age": 27,
        "department": "IT",
        "employee_id": "EMP004"
    },
    5: {
        "name": "Eva Davis",
        "age": 32,
        "department": "IT",
        "employee_id": "EMP005"
    }
}


j= filter( lambda k :  employees[k]["department"] == "IT" ,employees.keys())
print()
l = ['madam', 'racecar', 'Level', 'rafdar', 'deified', 'civic', 'rotor', 'noon', 'refer', 'wow']

# Lambda function to join the list into a single string
join_list = lambda lst: "".join(l)
joined_string = join_list(l)

print("Joined String:", joined_string)

# Python 3 code to demonstrate working of
# Tuple elements inversions
# Using map() + list() + sum()

# initializing tup
test_tup = ([7, 8], [9, 1], [10, 7])

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Tuple elements inversions
# Using map() + list() + sum()
res = sum(list(map(sum, list(test_tup))))

# printing result
print("The summation of tuple elements are : " + str(res))

test_list = [[('Gfg', 3)], [('best', 1)]]
cus_eles = [1, 2]
result_list = []
for i, row in enumerate(test_list):
    result_list.append(list(map(lambda x: x+(cus_eles[i],), row)))
print(result_list)


test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
out = [(5, 6, 7, 8), (6, 10), (7, 13)]

n = [test_list[0]]
for i in range(1,len(test_list)):
	if n[-1][0] == test_list[i][0]:
		n[-1]+=(test_list[i][1],)
		
	else:
		n.append(test_list[i])
print(n)



# Python3 code to demonstrate working of
# Join Tuples if similar initial element
# Using loop

# initializing list
test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]

# printing original list
print("The original list is : " + str(test_list))

# Join Tuples if similar initial element
# Using loop
res = []
for sub in test_list:
	if res and res[-1][0] == sub[0]:
		res[-1].extend(sub[1:])
	else:
		res.append([ele for ele in sub])
res = list(map(tuple, res))

# printing result
print("The extracted elements : " + str(res))
