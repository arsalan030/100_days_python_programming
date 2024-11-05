'''
Input : list1 = [1, 2, 3, 4, 5, 6] 
        list2 = [4, 5, 6, 7, 8] 
Output : Missing values in list1 = [8, 7] 
         Additional values in list1 = [1, 2, 3] 
         Missing values in list2 = [1, 2, 3] 
         Additional values in list2 = [7, 8] 
'''

list1 = [1, 2, 3, 4, 5, 6] 

list2 = [4, 5, 6, 7, 8] 
print(set(list1).difference(set(list2)))
print(set(list2).difference(set(list1)))
print(set(list1)&(set(list1)))

'''
GeeksforGeeks
Output : No. of vowels : 5
Explaination: The string GeeksforGeeks contains 5 vowels in it 4 letter of 'e' and 1 'o'.
'''
test_str = 'GeeksforGeeks'

string = "GeekforGeeks!"
vowels = "aeiou"

count = sum(string.count(vowel) for vowel in vowels)
print(count)

s1  = 'aacdb'
s2 = 'gafd'



s1 = 'abcs'
s2 = 'cxzca'


ss = set(s2) - set(s1) | set(s1) - set(s2)
print(''.join(ss))
s = set(s1) ^ set(s2)
s= ''.join(s)

print(s)

'''
u = set(k for s1  in s for k in s1  )
print(u)
uncommon = ''.join(set(s1 for s1  in s ))
print(uncommon)
'''


vowels = set("aeiou")


str = ' ABeeIghiObhkUul'
if vowels == set(''.join(i for i in str.lower() if i in vowels)) :
    print('accepted')
else:
    print('not accepted')
    print(set(''.join(i for i in str.lower() if i in vowels)),vowels)

