#Now we working on some basic questions of list in python

# Question n05
# write a python program to reversing a list :

lst = [2,2,3,4,5,6,7]

def reversing(lst):
    new_lst = lst[::-1]
    return new_lst

print(reversing(lst))

# another approch here we can solve this problem 

def revers(lst):
    left = 0
    size = len(lst)
    while left < size// 2:
        lst[left] , lst[size-left-1] = lst[size-left-1] , lst[left]
        left +=1
    return lst
    
    
    
print(revers(lst))


# here another approch to reverse the list this approche is insert approch

# input list
lst = [10, 11, 12, 13, 14, 15,15]
# the above input can also be given as
# lst=list(map(int,input().split()))
l = []  # empty list

# iterate to reverse the list
for i in lst:
    # reversing the list
    l.insert(0, i)
# printing result
print(l)

# write a python program count the acoourences of elemnt in a list:
def count_an_elemnt(lst ,e):
    count=sum(1 for i in lst if i == e)
    return count

print(count_an_elemnt(lst, 10))


    
def couns(lst):
    d= {i:lst.count(i) for i in lst}
    return d
print(couns(lst))


# write a python program to find sum and average list of python

def sum_and_average(lst):
    sam = sum(i for i in lst)
    return sam/len(lst),sam

print(sum_and_average(lst))


# Python program to find the sum
# and average of the list

L = [4, 5, 1, 2, 9, 7, 10, 8]


# variable to store the sum of
# the list
count = 0

# Finding the sum
for i in L:
	count += i

# divide the total elements by
# number of elements
avg = count/len(L)

print("sum = ", count)
print("average = ", avg)




# Python program to multiply all values in the
# list using traversal


def multiplyList(myList):

    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))


#Question  find the smallest number in list:
def find_smallaest(lst):
    temp = lst[0]
    for i in lst :
        if i <= temp:
            temp =  i
    return temp
# Python program to find smallest 
# number in a list

# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort()

# printing the first element




print("Smallest element is:", list1[0])



lst = [10, 11, 12, 13, 14, 15,15]
print(find_smallaest(lst))


#Qustion

# write a program to find second largest number in lst:
def find_second_largest(lst):
    maxx = max(lst[0],lst[1])
    second_max = min(lst[0],lst[1])
    for i in range(2,len(lst)):
        if lst[i]>maxx:
            second_max = maxx
            maxx = lst[i]
        elif lst[i] > second_max  and lst[i] != maxx:
            second_max = lst[i]
        elif second_max == maxx and lst[i] != second_max:
            second_max = lst[i]
    return f"second_max is {second_max}"

lst = [12,12,12,11,14,14,12,15]
        
print(find_second_largest(lst))



        



 