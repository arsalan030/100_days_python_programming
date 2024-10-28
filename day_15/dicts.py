'''
section H: Dictionary-Based String Manipulation
    7. Python Dictionary to Find Mirror Characters in a String
        ◦ Write a Python program to find mirror characters in a string based on a dictionary.
       Input:
       python
       Copy code
       str = 'abcd'
       Expected Output:
       python
       Copy code
       'dcba'
'''

def create_mirrir_string(string):


    reverse = string[::-1]

    mirror_map = dict(zip(reverse ,string))
   

    mirror_string = ""
    for i in range(len(string)):
        mirror_string += mirror_map[string[i]]
    return mirror_string

print(create_mirrir_string("bbaa"))



'''

    12. Find All Duplicate Characters in a String
        ◦ Write a Python program to find all duplicate characters in a given string.
       Input:
       python
       Copy code
       str = 'programming'
       Expected Output:
       python
       Copy code
       {'r': 2, 'g': 2, 'm': 2}'''


from collections import defaultdict

def find_duplicates(s):
    counts = defaultdict(int)
    for char in s:
        counts[char] += 1
    # Only keep items with a count greater than 1
    duplicates = {char: count for char, count in counts.items() if count > 1}
    return duplicates

print(find_duplicates("programming"))

'''
Section F: Complex Tasks with Dictionaries
    13. Python | Insertion at the Beginning in OrderedDict
        ◦ Use OrderedDict to insert an element at the beginning of a dictionary.
       Input:
       python
       Copy code
       from collections import OrderedDict
       d = OrderedDict([('A', 1), ('B', 2)])
    
'''

from collections import OrderedDict


d = OrderedDict([('A', 1), ('B', 2)])
d.update({'c': 3})
d.move_to_end('c' ,last = False)
print(d)

'''
    14. Kth Non-repeating Character Using List Comprehension and OrderedDict
        ◦ Find the Kth non-repeating character in a string using list comprehension and OrderedDict.
       Input:
       python
       Copy code
       s = 'geeksforgeeks'
       k = 3
       Expected Output:
       python
       Copy code

       'r' '''

