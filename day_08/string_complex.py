import re

# Initial list of strings
test_list = ["Good at 4", "Wake at 7", "Work till 6", "Sleep at 11"]

# Custom sort order list (numbers at the end of the strings)
subord_list = ["6", "7", "4", "11"]

# Creating a dictionary to map numbers to their custom sort index
temp_dict = {num: index for index, num in enumerate(subord_list)}

# Function to extract the number from the string and use it to get the sort index
def get_sort_key(string):
    # Extract the number at the end of the string
    match = re.search(r"(\d+)$", string)
    if match:
        num = match.group()  # Get the number as a string
        print(num)
        return temp_dict[num]  # Return the custom index from temp_dict
    return float('inf')  # Fallback in case no number is found (just in case)

# Sort the list of strings based on the custom index of the number at the end
sorted_list = sorted(test_list, key=get_sort_key)

# Print the sorted result
print("The sorted list:", sorted_list)




# Python3 code to demonstrate working of 
# Sort String by Custom Substrings
# Using sorted() + zip() + lambda + regex()
import re

# initializing list
test_list = ["Good at 4", "Wake at 7", "Work till 6", "Sleep at 11"]

# printing original list
print("The original list : " + str(test_list))

# initializing substring list 
subord_list = ["6", "7", "4", "11"]


# creating inverse mapping with index
temp_dict = {val: key for key, val in enumerate(subord_list)}

# custom sorting 
temp_list = sorted([[ele, temp_dict[re.search("(\d+)$", ele).group()]] \
				for ele in test_list], key = lambda x: x[1])
print(temp_list)
# compiling result
res = [ele for ele in list(zip(*temp_list))[0]]
		
# printing result 
print("The sorted list : " + str(res))


# Initializing String
test_str = "GeeksFosrGeeks"

# Removing char at pos 3
# using replace
new_str = test_str.replace('e', '')

# Printing string after removal
# removes all occurrences of 'e'
print("The string after removal of i'th character( doesn't work) : " + new_str)

# Removing 1st occurrence of s, i.e 5th pos.
# if we wish to remove it.
new_str = test_str.replace('s', '', 1)

# Printing string after removal
# removes first occurrences of s
print("The string after removal of i'th character(works) : " + new_str)


def vowel_count(str):
	# Creating a list of vowels
	vowels = "aeiouAEIOU"
	
	# Using list comprehension to count the number of vowels in the string
	count = len([char for char in str if char in vowels])
	
	# Printing the count of vowels in the string
	print("No. of vowels :", count)

# Driver code 
str = "GeeksforGeeks"

# Function Call
vowel_count(str)
c= []
vowels = "aeiouAEIOU"
for ch in str:
     if  ch in vowels:
          c.append(ch)

print(c)


# Python3 code to demonstrate working of
# Odd Frequency Characters
# Using list comprehension + Counter()

# check python program this string is symrticl and palindrome
s = "khokho"
n= len(s)//2
print(s[:n]==s[n:],n)
print(s,s[::-1])
l=0
r=len(s)-1
flag = False
while l<r//2:
     if s[l]==s[r]:
          flag =True
          l+=1
          r-=1


     else :
          flag = False
          break

print(flag)
          

def isymetrical(str):
     n= len(str)
     mid= n//2

     if  n%2 == 0:
         return str[:mid]==str[mid:]
    
     else:
         return str[:mid]==str[mid+1:]


str  = "khokho"
print(isymetrical(str))

def is_palindrome(str):
     return str == str[::-1]

print(is_palindrome(str))


# python program reverse string
str ="geeks quiz practice code"

def reversre_string(str):
     new_str = str.split()[::-1]
     s = ' '.join(new_str)
     s.rstrip
     print(s)
reversre_string(str)

def revered(str):
     newstr = str.split()
     l = []
     for i in newstr[::-1]:
          l.append(i)
     s = ' '.join(l)
     print(s)
revered(str)
    
          


# remove letters in string
def remove_letters(str,l):
     new_str = str.replace(l,"")
     print(new_str)

remove_letters('Geeks123For123Geeks',"123")

def remove_chrachters(str,l):
     s = [i for i in str if i not in l]
     s = ''.join(s)
     print(s)


remove_chrachters('Geeks123For123Geeks',"123")
     



def avoid_spaces(str):
     s = [i for i in str if i  != " "]
     s= "".join(s)
     print(s)

avoid_spaces(str)

     

          






           


