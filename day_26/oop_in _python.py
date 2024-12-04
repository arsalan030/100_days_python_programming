from typing import Any


class student:
    def __init__(self ,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_dettail(self):
        print(self.name,self.age,self.grade)


st = student('arsalan',25,'A')
st.get_dettail()

    
class rectangle :
    def __init__(self,length,breadth) -> None:
        self.length = length
        self.breadth = breadth
    
    def find_area(self):
        print(self.length * self.breadth)
    

r1= rectangle(32,34)
r1.find_area()



class square:
    def set_data(self,area):
        self.area = area

    def display_area(self):
        print(self.area**2)


c = square()
c.set_data(4)
c.display_area()

            
class employee:
    def __init__(self,salary,age,name) -> None:
        self.salary =  salary
        self.age = age
        self.name = name
    def  display_data(self):
        print(self.salary,self.age,self.name)
    
    def __del__(self):
        print('deleting object')



e1 = employee(35000,25,'arslan')
e1.display_data()
e2 = employee(35000,25,'arsalan')
e2.display_data()
#e1 = None
print(isinstance(e1,employee))

class number:
    count = 0
    def set_number(self,n):
        self.n = n
        number.count +=1

    def get_number(self):
        return self.n
        
    def print_n(self):
        print(self.n)

    def isnegative(self):
        if self.n< 0:
            print(True)
        else:
            print(False)
    def isdivisbale(self,n):
        if n==0:
            print(False)
        elif self.n % n ==0:
            print(True)
        else:
            print(False)
    def absolute_value(self):
        if self.n>0:
            print(self.n)
        else:
            print(self.n*-1)



x = number()
x.set_number(-2)
x.absolute_value()
x.isdivisbale(10)
x.isnegative()
xx = number()
xx .set_number(4)
print(number.count,x.count)

xxx = number()
xxx.set_number(0)

print(number.count,x.count)


def cell():
    print("xxxx")

def cell2():
    print("xxxxxxxxxxxxx")



class comple:
    def  __init__(self,imag,real) -> None:
        self.image = imag
        self.real = real
    
    def __str__(self) -> str:
        if self.real >= 0:
            return f"{self.real} + {abs(self.image)}i"
        else:
            return f"{self.real} + {abs(self.image)}i"
    
    def __add__(self,other):
        if isinstance(other,comple):
            return comple(self.real + other.real , self.image + other.image)
        
    def __sub__(self,other):
        if isinstance(other,comple):
            return  comple(self.real- other.real , self.image - other.image)
        

    def __mul__(self,other):
        if isinstance(other,comple):
            real_part = self.real * other.real 
            image_part =self.image * other.image
            return comple(real_part,image_part)
    def __truediv__(self, other):
        """Divide two complex numbers using / operator."""
        if isinstance(other, comple):
            denominator = other.real ** 2 + other.image ** 2
            if denominator == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            real_part = (self.real * other.real + self.image * other.image) / denominator
            imaginary_part = (self.image * other.real - self.real * other.image) / denominator
            return comple(real_part, imaginary_part)
        else:
            raise TypeError("Operand must be a ComplexNumber")

            

        
c1 =  comple(40,10)


c2 =  comple(33,4)

print(c1 /c2)



class matrix:
    def __init__(self,matrix = None) -> None:
        if matrix == None:
            self.matrix =  [[1,0,0],
                            [0,1,0],
                            [0,0,1],]
        elif len(matrix)!=3 or len(matrix[0]) !=3 :
            raise TypeError("matrix must be 3x3")
        else:
            self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str,row))for row in self.matrix])
    

    def __add__(self, other):
        """Add two 3x3 matrices."""
        if isinstance(other, matrix):
            result = []
            for i in range(3):
                result.append([self.matrix[i][j] + other.matrix[i][j] for j in range(3)])
            return matrix(result)
        else:
            raise TypeError("Operand must be a Matrix3x3.")

    def __sub__(self, other):
        """Add two 3x3 matrices."""
        if isinstance(other, matrix):
            result = []
            for i in range(3):
                result.append([self.matrix[i][j] - other.matrix[i][j] for j in range(3)])
            return matrix(result)
        else:
            raise TypeError("Operand must be a Matrix3x3.")






m1 =matrix([[1,2,3],
            [4,5,6],
            [7,8,9],])

m2 = matrix([[1,2,3],
            [4,5,6],
            [7,8,9],])
print(m1 + m2)
print(m1 - m2)



import math

class Solid:
    """Base class for all solids."""
    def surface_area(self):
        raise NotImplementedError("This method should be implemented by subclasses.")
    
    def volume(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

class Sphere(Solid):
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * self.radius**2

    def volume(self):
        return (4 / 3) * math.pi * self.radius**3

class Cube(Solid):
    def __init__(self, side):
        self.side = side

    def surface_area(self):
        return 6 * self.side**2

    def volume(self):
        return self.side**3

class Cylinder(Solid):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius**2 * self.height

def main():
    print("Choose a solid to calculate surface area and volume:")
    print("1. Sphere")
    print("2. Cube")
    print("3. Cylinder")
    
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        radius = float(input("Enter the radius of the sphere: "))
        sphere = Sphere(radius)
        print(f"Surface Area of Sphere: {sphere.surface_area():.2f}")
        print(f"Volume of Sphere: {sphere.volume():.2f}")

    elif choice == 2:
        side = float(input("Enter the side length of the cube: "))
        cube = Cube(side)
        print(f"Surface Area of Cube: {cube.surface_area():.2f}")
        print(f"Volume of Cube: {cube.volume():.2f}")

    elif choice == 3:
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        cylinder = Cylinder(radius, height)
        print(f"Surface Area of Cylinder: {cylinder.surface_area():.2f}")
        print(f"Volume of Cylinder: {cylinder.volume():.2f}")

    else:
        print("Invalid choice. Please choose a valid solid.")

#if __name__ == "__main__":
  #  main()


class bank_account:
        def __init__(self,account_number,balance,account_holder) -> None:
            self.account_number = account_number
            self.___balance = balance
            self.account_holder = account_holder
        
        def deposit_money__(self,other):
            self.___balance += other
            
        
        def with_drawa_money(self,other):
            self.___balance -= other
            
        def display_balance(self):
            print(self.___balance,self.account_holder,self.account_number)
        
b1  =  bank_account(1234,2000,'arsalan')
b1.deposit_money__(23000)
b1.with_drawa_money(5000)

b1.display_balance()



class tim :
    def __init__(self,hours,minutes,second):
        self.hours = hours
        self.minutes  = minutes
        self.second = second
        self.normalize_time()
    
    def normalize_time(self):
        """
        Adjust the time values so that seconds and minutes remain within their proper range.
        """
        self.minutes += self.second // 60
       
        self.second = self.second % 60


        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60
    
    def __str__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.second:02d}"
    
    def __add__(self,other):
        self.hours += other.hours
        self.minutes += other.minutes
        self.second += other.second
        return tim(self.hours,self.minutes,self.second)
    def __sub__(self, other):
        """
        Subtract one Time object from another and return a new normalized Time object.
        Handles negative time gracefully.
        """
        total_seconds_self = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_seconds_other = other.hours * 3600 + other.minutes * 60 + other.seconds
        total_seconds_result = max(0, total_seconds_self - total_seconds_other)

        # Convert back to hours, minutes, and seconds
        hours = total_seconds_result // 3600
        total_seconds_result %= 3600
        minutes = total_seconds_result // 60
        seconds = total_seconds_result % 60

        return tim(hours, minutes, seconds)
        
    


t1 = tim(6,30,10)
t2 = tim(6,30,10)
print(t1+t2)






    






        
