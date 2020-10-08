def my_enum(lst1):
    lst=[]
    for i in range(len(lst1)):
        #index,fruit=i,lst1[i]
        #tup=(index,fruit)
        #lst.append(tup)
        lst.append((i,lst1[i]))
    return(lst)

bigbasket=['apple','banana','cherry','orange','mango']
print(my_enum(bigbasket))