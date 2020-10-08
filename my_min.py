def my_min(lst):
    a=lst[0]
    for i in range(1,len(lst)):
        if lst[i]<a:
            a=lst[i]
    return a

list=[-2,-9,-6,-4,-4,-5,-1]
print(my_min(list))