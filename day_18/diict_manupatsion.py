
# Python3 code to demonstrate working of 
# Factors Frequency Dictionary
# Using loop

# initializing list
test_list = [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]

# printing original list
print("The original list : " + str(test_list))

res = dict()

# iterating till max element 
for idx in range(1, max(test_list)):
	res[idx] = 0
	for key in test_list:
		
		# checking for factor 
		if key % idx == 0:
			res[idx] += 1
		
# printing result 
print("The constructed dictionary : " + str(res))

'''
Input: test_dict = {‘Manjeet’: [1], ‘Akash’: [1, 8, 9]} 
Output: {‘Manjeet’: [], ‘Akash’: [8, 9]} 
'''
test_dict = {'Manjeet': [1], 'Akash': [1, 8, 9]} 


data = [k for kk in test_dict.values() for k in kk ]

mapped = Counter(data)
print(mapped)
new_dict = {k :[kk for kk in v if mapped[kk]==1] for k,v in test_dict.items() }
print(new_dict)
'''
test_dict = {‘gfg’ : {‘x’ : 5, ‘y’ : 6, ‘z’: 3}, ‘best’ : {‘x’ : 8, ‘y’ : 3, ‘z’: 5}} 
ottput [(‘x’, (5, 8)), (‘y’, (6, 3)), (‘z’, (3, 5))] I
'''

test_dict = {'gfg' : {'x' : 5, 'y' : 6, 'z': 3}, 'best' : {'x' : 8, 'y' : 3, 'z': 5}} 


mapp= [(key,tuple(c[key] for c in test_dict.values()))for key in test_dict['gfg']]

# Using list comprehension + generator expression
res = [(key, tuple(sub[key] for sub in test_dict.values())) 
                               for key in test_dict['gfg']]
print(mapp)



from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    
    for word in words:
        # Sort each word to create a unique key for its anagram group
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    
    # Return grouped anagrams as a list of lists
    return list(anagrams.values())

# Example usage
words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(group_anagrams(words))  # Expected Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


lst = [1,3,5,7,9]
target = 456


def remote_probelm(lst,target):
	new_clossest = ''
	for i in str(target):
		if int(i) not in lst:
			closest = min(lst, key=lambda x: abs(x - int(i)))
			new_clossest += str(closest)
		else:
			new_clossest += i
	return new_clossest

print(remote_probelm(lst,target))

closest = min(lst, key=lambda x: abs(x - target))
print(closest)
			



		
	
# Example usage

def closest_number(lst, target):
    # Sort the list and make sure it contains unique integers
    lst = sorted(set(lst))
    target_str = str(target)
    closest_result = ""
    
    # Iterate over each digit in the target
    for i, digit in enumerate(target_str):
        digit = int(digit)
        
        # Find the closest digit in lst
        if digit in lst:
            closest_result += str(digit)
        else:
            # Find the nearest digit either smaller or larger, if possible
            lower = [x for x in lst if x < digit]
            higher = [x for x in lst if x > digit]
            
            if lower and higher:
                # Choose the closer one, or the smaller one if equidistant
                closest_digit = min(lower + higher, key=lambda x: (abs(x - digit), x))
            elif lower:
                closest_digit = max(lower)
            else:
                closest_digit = min(higher)
            
            closest_result += str(closest_digit)
            # Use the smallest digit from lst for all remaining places
            if closest_digit < digit:
                closest_result += str(max(lst)) * (len(target_str) - i - 1)
            else:
                closest_result += str(min(lst)) * (len(target_str) - i - 1)
            break  # Remaining digits are set, so exit loop

    return int(closest_result)

# Example usage
lst = [1, 3, 5, 7, 9]
target = 846
print(closest_number(lst, target))  # Expected Output: 513



