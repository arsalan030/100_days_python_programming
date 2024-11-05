
biniary_set = set('10')
print(biniary_set)
str = '10101010101'
if biniary_set in set(str):
    print('yes')
else:
    print('no')



set1 = {"abcdefgh", "geeksforgeeks",
                 "lmnopqrst", "abc"}

set2= {"ijklmnopqrstuvwxyz", 
                 "abcdefghijklmnopqrstuvwxyz", 
                 "defghijklmnopqrstuvwxyz"}
lst=[(''.join(sorted(list(set(k+v))))) for v in set2 for k  in set1 if ''.join(sorted(list(set(k+v))))== "abcdefghijklmnopqrstuvwxyz"]
print(lst)


s = "the big dwarf only jumps"
s = ''.join(s.split(' '))
print(set(s))
#he string S is occurred only once.

# Function to Check whether a given string is Heterogram or not
def heterogram(input):
	# separate out list of alphabets using list comprehension
	# ord function returns ascii value of character
	alphabets = [ch for ch in input if (
		ord(ch) >= ord('a') and ord(ch) <= ord('z'))]
	# convert list of alphabets into set and
	# compare lengths
	if len(set(alphabets)) == len(alphabets):
		print('Yes',alphabets,set(alphabets))
        
	else:
		print('No')



# Driver program
if __name__ == "__main__":
	input = 'the big dwarf only jumps'
	heterogram(input)
    
arr = [[1, 2, 2, 4, 3, 6],
              [5, 1, 3, 4],
              [9, 5, 7, 1],
              [2, 4, 1, 3]]
cobine = set([i for ari in arr  for i in ari ])
print(cobine)



# Function to combine n arrays
	
def combineAll(input):
		
	# cast first array as set and assign it
	# to variable named as result
	result = set(input[0])
	
	# now traverse remaining list of arrays
	# and take it's update with result variable
	for array in input[1:]:
		result.update(array)
	
	return list(result)
	
# Driver program
if __name__ == "__main__":
	input = [[1, 2, 2, 4, 3, 6],
			[5, 1, 3, 4],
			[9, 5, 7, 1],
			[2, 4, 1, 3]]
	print (combineAll(input))

from functools import reduce

lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]



intersection = reduce(lambda acc, x: acc + [x] if x in lst2 and x not in acc else acc, lst1, [])

print(intersection)

#This code is contributed by Rayudu.


