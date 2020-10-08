def my_sorted(lst):
    res=[]
    #print(len(lst))
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i!=j:
                if lst[i]>lst[j]:
                    temp=lst[i]
                    lst[i]=lst[j]
                    lst[j]=temp
    return lst 
def my_sorted(lst,reverse):
    res=[]
    #print(len(lst))
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i!=j:
                if lst[i]>lst[j]:
                    temp=lst[i]
                    lst[i]=lst[j]
                    lst[j]=temp
    return lst     
input=[100,2,1,4,12,6,1,9]

#print(my_sorted(input,False))
print(my_sorted(input))