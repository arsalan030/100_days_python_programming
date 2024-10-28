''' Input : test_dict = {"Gfg" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]} 
Output : "Gfg" 
Explanation : "Gfg" having max unique elements i.e 5.  '''

test_dict = {"Gfg" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}

def find_most_unieq_values(test_dict):
	
    unieq = {}
    for k,v in test_dict.items():
        unieq[len(set(v))] = k
		
    print(unieq)
		
    maxx = max(sorted(unieq.items(),key=lambda d : d[0]))
    print(maxx)
	
find_most_unieq_values(test_dict)

d= max(sorted({len(set(v)): k for k,v in test_dict.items()}.items(),key=lambda d:d[1]))
print(d)

'''		
Input : test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8] 
Output : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]} 
Explanation : Similar items grouped together on occurrences. 
'''


test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8] 



from collections import defaultdict ,Counter ,OrderedDict

def group_similar_ele(test_list):
	data = defaultdict(list)
	for i in test_list:
		
		data[i] .append(i)
	return data

print(group_similar_ele(test_list))


d = {k : [k]*v for k,v in Counter(test_list).items()}
print(d)

	
'''
Input : str = geeksforgeeks, k = 3
Output : r
First non-repeating character is f,
second is o and third is r.

Input : str = geeksforgeeks, k = 2
Output : o
'''
st = 'geeksforgeeks'

k =3
data = Counter(st)
d = [k for k in data if data[k]==1]
print(d)
if len(d) < k:
      print(f"nonreapting chrachter is len then kth,{d}")
else:
    print(f"nonreapting chrachter is kth elmenet is,{d[k-1]}")
      



