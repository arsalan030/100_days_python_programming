# question find the matching chrachter in string 
str1  = "abcded"
str2 = "defhaia"
matching = [i for i in str1 if i in str2] + [i for i in str2 if i in str1]
print(len(set(matching)),matching)

#question python program find least frequancy in str
str3 = "geeksforgeeks"
s= {i:str3.count(i)for i in str3}

freq = min(s,key =s.get)
print(freq)
odd_freq = []
for i in str3:
    if s[i] % 2 !=0:
        odd_freq.append(i)
print(odd_freq)



from itertools import groupby

# initializing string
test_str = "geekksforgggeeks"

# printing original string

# Consecutive characters frequency
res = [len(list(j)) for _, j in groupby(test_str)]

# printing result
print("The Consecutive characters frequency : " ,res)

# question rotate string clock wise anti clock wise
s = "geekforgeeks"
d = 2
clockwise = s[d:] + s[:d]
anticlock = s[-d:]+ s[:-d]
print(clockwise,anticlock)

# initializing string
test_str = 'geeksforgeeks is best for geeks. A geek should take interest.'

# initializing word
que_word = 'geek'

# initializing dictionary to store character frequencies
freq_dict = {}

# loop through the string and count successive character frequencies
for i in range(len(test_str)-1):
	if test_str[i:i+len(que_word)] == que_word:
		char = test_str[i+len(que_word)]
		if char in freq_dict:
			freq_dict[char] += 1
		else:
			freq_dict[char] = 1

# print the result
print('The Characters Frequency is:', freq_dict)

test_list = ["geekforgeeks", "is", "best", "for", "geeks"]
 
# printing original list
print("The original list is : " ,test_list)
 
# initializing K 
K = 'e'
 
# "-" sign used to reverse sort
res = sorted(test_list, key = lambda ele: -ele.count(K))
# printing results
print("Sorted String : " ,res)