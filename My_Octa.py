def my_octa(n):
    lst=[]
    while(n>0):
        r=n%8
        n=n//8
        lst.insert(0,str(r))
    string="".join(lst)
    return "0o"+string


num=20
#num=int(input("enter the integer number for bbinary conversion"))

print(my_octa(num))