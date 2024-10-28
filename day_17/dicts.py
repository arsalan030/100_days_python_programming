'''
Input : Dict = ["go","bat","me","eat","goal","boy", "run"]
        arr = ['e','o','b', 'a','m','g', 'l']
Output : go, me, goal. 

'''

words = ["go","bat","me","eat","goal","boy", "run"]
arr = ['e','o','b', 'a','m','g', 'l']


def find_possiable_word(words,arr):
      data = Counter(arr)
      l=[]
      flag=  1


      for i in words:
           word_d = Counter(i)
           for k in word_d.keys():
                  if word_d[k] == data[k]:
                     flag = 0
                  else:
                         flag =1
           if flag == 0:
                  l.append(i)
      return l
           
      
                 

                        
     
            
                   
      

print(find_possiable_word(words,arr))
            


# Function to print words which can be created
# using given set of characters



def charCount(word):
	dict = {}
	for i in word:
		dict[i] = dict.get(i, 0) + 1
	return dict


def possible_words(lwords, charSet):
	for word in lwords:
		flag = 1
		chars = charCount(word)
		for key in chars:
			if key not in charSet:
				flag = 0
			else:
				if charSet.count(key) != chars[key]:
					flag = 0
		if flag == 1:
			print(word)

if __name__ == "__main__":
	input = ['goo', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
	charSet = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
	possible_words(input, charSet)







'''
The original dictionary is : {'gfg': {'Manjeet': 5, 'Himani': 10}, 'is': {'Manjeet': 8, 'Himani': 9}, 'best': {'Manjeet': 10, 'Himani': 15}}
The required key is : best
'''

d = {'gfg': {'Manjeet': 5, 'Himani': 10}, 'is': {'Manjeet': 8, 'Himani': 9}, 'best': {'Manjeet': 10, 'Himani': 15}}

def maximum_key(d,key='Manjeet'):
       max_key  = 0

       for k,sub in d.items():
              if  sub[key] > max_key:
                     max_key = sub[key]
       return k
              
                     
print(maximum_key(d))

key='Manjeet'
maxx_key = max(d ,key= lambda sub: d[sub][key])
print(maxx_key)
       
       
'''
Input : test_dict = {Gfg : {“a” : 7, “b” : 9, “c” : 12}, is : {“a” : 15, “b” : 19, “c” : 20}, ‘best’ :{“a” : 5, “b” : 10, “c” : 2}}, temp = “b” 
Output : [9, 10, 19] 
Explanation : All values of “b” key are extracted. 
'''

test_dict = {'Gfg' : {"a" : 7, "b" : 9, "c" : 12}, 'is ': {"a" : 15, "b" : 19, "c" : 20}, 'best' :{"a" : 5, "b" : 10, "c" : 2}}     
temp = "b"

all_val= [test[temp] for test in test_dict.values()]
print(all_val)




from collections import Counter

# initializing dictionary
test_dict = {'Manjeet': [1, 4, 5, 6],
			'Akash': [1, 8, 9],
			'Nikhil': [10, 22, 4],
			'Akshat': [5, 11, 22]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Remove duplicate values across Dictionary Values
# Using Counter() + list comprehension
cnt = Counter()
for idx in test_dict.values():
	cnt.update(idx)
res = {idx: [key for key in j if cnt[key] == 1]
	for idx, j in test_dict.items()}

# printing result
print("Uncommon elements records : " + str(res))




