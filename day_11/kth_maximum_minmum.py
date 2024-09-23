# problem is that find kth maximum and minium elements in tuple
k = 3
tupl  = (1,9,5,4,3,7,12,15,99)
# first we sort the tuple then iterate the with enumerate throught index 
tupl = sorted(tupl)
print(tupl)
max_min = []
for  ind ,val in enumerate(tupl):
    if ind < k or ind >= len(tupl)-k:
        max_min.append(val)
print(max_min)

# usiing higher order funcatsion to solve this problem
max_min = map(lambda x  : x[1] if x[0] < k or x[0]>= len(tupl)-k else None,enumerate(sorted(tupl)))
max_min  = filter(lambda x : x is not None ,max_min)
print(list(max_min))