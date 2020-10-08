def my_max(lst):
    a=lst[0]
    for i in range(1,len(lst)):
        #print(i)
        if lst[i]>a:
            a=lst[i]
    return a

list=[-1,-2,-9,-6,-4,-4]
print(my_max(list))