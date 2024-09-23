#problem is that row wise elemnet addistion in tuple
test_list = [[('Gfg', 3)], [('best', 1)]]
cus_eles = [1, 2] 
# add this tuples in to test_list
test_list = [[sub + (cus_eles[ind],)for sub in val]for ind ,val in  enumerate(test_list)]
print(test_list)

# another approch to solve this problem using high order funactsions


test_list = map(
    lambda x: [x[1][0] + (cus_eles[x[0]],)],  # Add cus_eles element to the second part of the tuple
enumerate(test_list)
)   
print(list(test_list))



# problem is that multiply adjacent element

from itertools import starmap
tple = (1,3,4,5,6)
pairs = zip(tple, tple[1:])
result = starmap(lambda x, y: x * y, pairs)
print(list(result)) 

ple =  (tple[i]*tple[i+1]for i in range(0 ,len(tple)-1))
print(list(ple))


