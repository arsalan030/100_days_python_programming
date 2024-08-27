# question 
# revers the string in python

str = "arsalan is a prograamer"
new_str =  str.split(' ')
new_str = ' '.join(new_str[::-1])
print(new_str)

# question 
# remove the ith chrachter in python
str= "geeks123for123geeks"
new_str = str.replace('123','')
print(new_str)
news=""
for i in str:
    if i in"123":
        continue
    else:
        news+=i
       

print(news)



# question
# # Python3 code to demonstrate working of 
# Avoid Spaces in Characters Frequency
# Using isspace() + sum()

# initializing string
test_str = 'geeksforgeeks 33 is best'

# printing original string
print("The original string is : " +(test_str))

# isspace() checks for space 
# sum checks count 
res = sum(not chr.isspace() for chr in test_str)
	
# printing result 
print("The Characters Frequency avoiding spaces : " ,int(res)) 

test_str = 'geeksforgeeks 33 is best'
length = 0 
for i in test_str:
    if  i == " ":
        continue
    else:
        length+=1
print(length)


# Python code 
# To print even length words in string 

#input string 
n="This is a python language"
#splitting the words in a given string
s=n.split(" ") 
for i in s: 

#checking the length of words
    if len(i)%2==0: 
        print(i)

    # this code is contributed by gangarajula laxmi



# Python3 code to demonstrate working of
# Uppercase Half String
# Using upper() + loop + len()

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " +(test_str))

# computing half index
hlf_idx = len(test_str) // 2

res = ''
for idx in range(len(test_str)):

	# uppercasing later half
	if idx >= hlf_idx:
		res += test_str[idx].upper()
	else:
		res += test_str[idx]

# printing result
print("The resultant string : " ,res)



# Python program to capitalize
# first and last character of
# each word of a String

s = "welcome to geeksforgeeks"
print("String before:", s)
a = s.split()
res = []
for i in a:
	x = i[0].upper()+i[1:-1]+i[-1].upper()
	res.append(x)
res = " ".join(res)
print("String after:", res)


#question
# python program check string if conatin all vowels in string
def check(string):
	string = string.replace(' ', '')
	string = string.lower()
	vowel = [string.count('a'), string.count('e'), string.count(
		'i'), string.count('o'), string.count('u')]

	# If 0 is present int vowel count array
	if vowel.count(0) > 0:
		return('not accepted')
	else:
		return('accepted')


# Driver code
if __name__ == "__main__":

	string = "SEEquoiaL"

	print(check(string))



