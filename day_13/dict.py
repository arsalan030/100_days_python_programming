'''   5. Sort List of Dictionaries by Values Using itemgetter
        ◦ Sort a list of dictionaries by a specific key using itemgetter.
       Input:
       python
       Copy code
       from operator import itemgetter
       dicts = [{'name': 'Tom', 'age': 20}, {'name': 'John', 'age': 25}, {'name': 'Mark', 'age': 22}]
       Expected Output:
       python
       Copy code
       [{'name': 'Tom', 'age': 20}, {'name': 'Mark', 'age': 22}, {'name': 'John', 'age': 25}] 
       
'''


dicts = [{'name': 'Tom', 'age': 20}, {'name': 'John', 'age': 25}, {'name': 'Mark', 'age': 22}]


d = sorted(dicts ,key = lambda i : i['name'])
print(d) 

'''
    6. Merging Two Dictionaries
        ◦ Write a Python program to merge two dictionaries.
       Input:
       python
       Copy code
       d1 = {'a': 100, 'b': 200}
       d2 = {'x': 300, 'y': 400}
       Expected Output:
       python
       Copy code
       {'a': 100, 'b': 200, 'x': 300, 'y': 400}
'''

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 400}

d3 = {**d1,**d2}
print(d3)
import itertools 

de =  itertools.chain(d1,d2)
print(d3)
'''

    7. Create Grade Calculator
        ◦ Write a Python program to calculate grades based on student marks using a dictionary.
       Input:
       python
       Copy code
       student_scores = {'John': 85, 'Jane': 92, 'Dave': 76}
       Expected Output:
       python
       Copy code
       {'John': 'B', 'Jane': 'A', 'Dave': 'C'}
'''


def grade_calculater(students):
    for i in students.keys():
        if students[i] >= 60 and students[i] <80:
            students[i] = 'B'
        elif students[i]>=80 and students[i] <90:
            students[i] =    'A' 
        elif students[i]>= 90:
            students[i] = 'A+'
        else:
            students[i] = 'F'
    return students

student = {'John': 85, 'Jane': 92, 'Dave': 76}
print(grade_calculater(student))