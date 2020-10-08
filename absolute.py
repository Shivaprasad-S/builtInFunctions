def abso(num):
    #if num<0:
    #   return (-num)
    #return num
    return -num if num<0 else num



number=float(input("enter a number to check\n"))
print("Absolute value of given number is ",abso(number))