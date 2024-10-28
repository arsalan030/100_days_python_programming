
from collections import defaultdict ,Counter
a= ["arsalan", "ahmed","ahsan","ali","arsalan","ahmed"]

def find_winner(a):
      dat = Counter(a)
      d = defaultdict(list)
      for k,v in dat.items():
            d[v].append(k)
      maxx = max(sorted(d.items(),key=lambda d :d[1]))[0]
      print(maxx)

      if  len(d[maxx]) > 1:
            print(sorted(d[maxx])[0])
      else:
            print(d[maxx][0])

find_winner(a)

test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
del test_dict["Anuradha"
              ]
removed_value = test_dict.pop('Manjeet','ket error')


print(removed_value,test_dict)



'''
Input : test_str = geekforgeeks best for geeks, repl_dict = {“geeks” : “all CS aspirants”} 
Output : geekforgeeks best for all CS aspirants 
Explanation : “geeks” word is replaced by lookup value. 

'''
test_str = 'geekforgeeks best for geeks'
t =test_str.split(' ')
print(test_str)
epl_dict = {"best" : "good and better", "geeks" : "all CS aspirants"}
a = ("".join(t[i])+" "+ ep for ep in epl_dict.values()for i in range(len(t)))
print(list(a)[0])





# Python3 code to demonstrate working of 
# Replace words from Dictionary
# Using split() + join() + get()

# initializing string
test_str = 'geekforgeeks best for geeks'




# lookup Dictionary
lookp_dict = {"best" : "good and better", "geeks" : "all CS aspirants"}

# performing split()
temp = test_str.split()
res = []
for wrd in temp:
	
	# searching from lookp_dict
	res.append(lookp_dict.get(wrd, wrd))
	
res = ' '.join(res)

print(res)


'''
Input : s1 = ABHISHEKsinGH
      : s2 = gfhfBHkooIHnfndSHEKsiAnG
Output : Possible
'''

def creating_sring(s1,s2):
      
      s2 = Counter(s2)
      s = ''.join(k for k in s1 if k in s2)

      if  s == s1:
            return True
      else:
            False



s1 = 'ABHISHEKsinGH'
s2 = 'gfhfBHkooIHnfndSHEKsiAnG'
#print(creating_sring(s1,s2))



s1 = 'ABHISHEKsinGH'
s2 = 'gfhfBHkooIHnfndSHEKsiAnG'


def creating_dict(s1,s2):
        s1 = Counter(s1)
        s2 = Counter(s2)
        

     
    
print(creating_dict(s1,s2))
    

     

s1 = 'ABHISHEKsinGH'
s2 = 'gfhfBHkooIHnfndSHEKsiAnG'
print(creating_dict(s1,s2))



