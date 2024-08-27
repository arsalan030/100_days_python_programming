
def check():
    str = 'level'


    left = 0
    right = len(str)-1
    a = len(str)/2

    while left <= a//2:
            if str[left] == str[right] :
                left +=1
                right-=1
            else:
                return f"{str} is not palindorme"
    else:
         return f"{str} is palindrome string"


print(check())