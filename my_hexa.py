def my_hexa(n):
    lst=[]
    while(n>0):
        r=n%16
        n=n//16
        if r==10:
            r='A'
        elif r==11:
            r='B'
        elif r==12:
            r='C'
        elif r==13:
            r='D'
        elif r==14:
            r='E'
        elif r==15:
            r='F'
        else:
            r=r
        lst.insert(0,str(r))
    string="".join(lst)
    return "0x"+string


num=60
#num=int(input("enter the integer number for bbinary conversion"))

print(my_hexa(num))