# problem is that join the tuples element if initial elment is same of tuples 
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
new_list = [test_list[0]]
for i in range(1,len(test_list)):
    if test_list[i][0] == new_list[-1][0] :
        new_list[-1]+= test_list[i][1:]
    else:
        new_list.append(test_list[i])

print(new_list)

