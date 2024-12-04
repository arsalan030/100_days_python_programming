class base:
    def __method(self):
        print("in base__method")
    def fun(self):
        self.__method()

class derived(base):
    def __method(self):
        print('in derived__method')
    
    def new_func(self):
        self.__method()


b =base()
b.fun()
d = derived()
d.fun()
d.new_func()



class b1:
    def __init(self,name):
        self.name =  name
    
    def __del__(self):
        print("distruucter of b1")

class b2:
    def __init__(self,last_name) -> None:
        self.last_name = last_name
        print(self.last_name)
    
    def __del__(self):
        print("distruucter of b2")
    

class D(b2,b1):
   

    def __del__(self):
        print("distruucter of D")

d= D('ahmed')



from abc import ABC ,abstractmethod
class shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class circle(shape):
    def draw(self):
        print("draw")
    

c = circle()
c.draw()


'''

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

class DecorateAllMethods:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        for attr, value in cls.__dict__.items():
            if callable(value):
                setattr(cls, attr, my_decorator(value))


class MyClass(DecorateAllMethods):
    def method1(self):
        print("Executing method1")
    
    def method2(self):
        print("Executing method2")

obj = MyClass()
obj.method1()
obj.method2()



class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
      
        #we will return a string 
        return self.word+' ( '+self.meaning+' )'
      
flash = []
print("welcome to flashcard application")

#the following loop will be repeated until
#user stops to add the flashcards

while(True):
    word = input("enter the name you want to add to flashcard : ")
    meaning = input("enter the meaning of the word : ")
    
    flash.append(flashcard(word, meaning))
    option = int(input("enter 0 , if you want to add another flashcard : "))
    
    if(option):
        break
        
# printing all the flashcards 
print("\nYour flashcards")
for i in flash:
    print(">", i)
'''





# This is simplest Student data management program in python

# Create class "Student"
class Student:

# Constructor
	def __init__(self, name, rollno, m1, m2):
		self.name = name
		self.rollno = rollno
		self.m1 = m1
		self.m2 = m2

	# Function to create and append new student
	def accept(self, Name, Rollno, marks1, marks2):

# use ' int(input()) ' method to take input from user
		ob = Student(Name, Rollno, marks1, marks2)
		ls.append(ob)

	# Function to display student details
	def display(self, ob):
		print("Name : ", ob.name)
		print("RollNo : ", ob.rollno)
		print("Marks1 : ", ob.m1)
		print("Marks2 : ", ob.m2)
		print("\n")

	# Search Function
	def search(self, rn):
		for i in range(ls.__len__()):
			if(ls[i].rollno == rn):
				return i

	# Delete Function
	def delete(self, rn):
		i = obj.search(rn)
		del ls[i]

	# Update Function
	def update(self, rn, No):
		i = obj.search(rn)
		roll = No
		ls[i].rollno = roll


# Create a list to add Students
ls = []
# an object of Student class
obj = Student('', 0, 0, 0)

print("\nOperations used, ")
print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")

# ch = int(input("Enter choice:"))
# if(ch == 1):
obj.accept("A", 1, 100, 100)
obj.accept("B", 2, 90, 90)
obj.accept("C", 3, 80, 80)

# elif(ch == 2):
print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
	obj.display(ls[i])

# elif(ch == 3):
print("\n Student Found, ")
s = obj.search(2)
obj.display(ls[s])

# elif(ch == 4):
obj.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
	obj.display(ls[i])

# elif(ch == 5):
obj.update(3, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):
	obj.display(ls[i])

# else:
print("Thank You !")

