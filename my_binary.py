def my_binary(n):
    lst=[]
    while(n>0):
        r=n%2
        n=n//2
        lst.insert(0,str(r))
    return "".join(lst)


#num=1
num=int(input("enter the integer number for bbinary conversion"))

print(my_binary(num))