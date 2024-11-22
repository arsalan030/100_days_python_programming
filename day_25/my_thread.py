
import threading 

from threading import *
import time




'''
def func1():
    for i in range(5):
        print("hellow world")


def func2():
    for i in range(5):
        print("i love you Arsalan")

th1 = threading.Thread(name='my first thread',target=func1)
th2 = threading.Thread(target=func2)
th1.start()
th2.start()
th2.join()




print("that is main thread")
t = threading.current_thread()
print(t.name)




# write a program  that calculates the squares and cubes of first 6 odd number s through funacstions that are exuted sequantially 
# a delay of 0.5 senconds after calculatsion of each  square value report time required of each exiscuation program
# '''

def squaree_number():
    
    print("calculating_square")
    for n in range(5):
        time.sleep(0.5)
        print(f"n= ", n ,"square of n = ", n * n)

def cubes_number():
    print("cubes)_number")
    for n in range(5):
        time.sleep(0.5)
        print("n= ", n ,"cube of n = ", n * n*n)

'''

arr = [1,3,5,7,9]
startime = time.time()
squaree_number(arr)
cubes_number(arr)
endtime=  time.time()
print("time_required = : " , endtime - startime, 'sec')

'''
starttime= time.time()

t1 = threading.Thread(target=squaree_number,name="square_thread")

t2 = threading.Thread(target=cubes_number,name="cube_thread")

t1.start()
t1.join()

t2.start()


t2.join()

endtime = time.time()

print("time required" ,endtime - starttime,"sec")

for i in range(5):
    print("heloow  arsalan")




