# swap the values of variable without using the  third varibale
a,b = 5 ,10
b,a = a,b
print(a,b)


#94. Write a Python program to calculate the sum of all prime numbers in a given list of positive



def is_prime(num):
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if num == 2:
        return True  # 2 is a prime number
    if num % 2 == 0:
        return False  # Exclude other even numbers
    
    # Check divisors up to the square root of the number
    for i in range(3, int(num**0.5) + 1, 2):
       
        if num % i == 0:
            return False
    return True
def sum_of_prime(lst):
    summ = 0
    for i in lst:
        if is_prime(i):  # Check if the number is prime
            summ += i
    return summ

# Test the function
lst = [1, 3, 4, 7, 9,4,6,25,36,77,77,45,45,2,4,5,]
print(sum_of_prime(lst))  # Output: 10 (3 + 7)



# 93. Write a Python program that takes an integer and rearranges the digits to create two maximum and minimum numbers. 
def create_maximum_and_minmum(n):
  a = ' '.join(str(n)).split(' ')
  a.sort()
 
  maximum = int(''.join(a))

  a.reverse()
  minimum = int(''.join(a))
  return maximum,minimum
  
print(create_maximum_and_minmum(1237564499))



# Write a Python program that checks whether the absolute difference between two consecutive digits is two or not. Return true otherwise false
def check_absolute_difference(n):
    # Convert the number to a list of digits
    digits = list(map(int, str(n)))
    
    # Iterate through consecutive digit pairs
    for i in range(len(digits) - 1):
        # Check if the absolute difference is not equal to 2
        if abs(digits[i] - digits[i + 1]) != 2:
            return False  # Return False if any pair fails the condition
    
    return True  # Return True if all pairs satisfy the condition

# Sample Data
print(check_absolute_difference(666))    # Output: False
print(check_absolute_difference(3579))   # Output: True
print(check_absolute_difference(2468))   # Output: True
print(check_absolute_difference(20420))  # Output: False



#Write a Python program to check if a given number is a Harshad number or not. Return True if the number is Harshad otherwise False.

def harshed_number(n):
  summ = 0
  a = n
  for i in range(len(str(n))):
    number = n//10
    summ += i
    n = n%10
  if a% summ  == 0:
    return True
  else:
    return False
  
print(harshed_number(666))


#89. Write a Python program to check if a given number is a repdigit number or not. If the given number is repdigit return true otherwise false

def find_repdgit_numbrr(n):
   number = list(map(int,str(n)))
   for i in number[1:]:
      if number[0] != i:
         return False
   return True

print(find_repdgit_numbrr(666))


def find_disarium_number(n):

   lst =list(map(int,str(n)))   
   summ = 0
   for index,val in enumerate(lst,1):
     summ += val** index
    
   if summ == n:
      return True
   else:
      return False
      
find_disarium_number(175)

#87. Write a Python program to cap a number within the inclusive range specified by the given boundary values x and y.


def cap_number(num, x, y):
    # Ensure x is the lower boundary and y is the upper boundary
    lower = min(x, y)
    upper = max(x, y)
    
    # Cap the number
    if num < lower:
        return lower
    elif num > upper:
        return upper
    else:
        return num

# Examples
print(cap_number(3, 5, 10))   # Output: 5
print(cap_number(15, 5, 10))  # Output: 10
print(cap_number(7, 5, 10))   # Output: 7
print(cap_number(12, 15, 10)) # Output: 12

   
   
         
      