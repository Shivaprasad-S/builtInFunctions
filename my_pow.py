def my_pow(num1,num2):
    #num1=num1[0]
    #num2=num1[1]
    counter=1
    prod=1


    while counter<=num2:
        prod=prod*num1
        counter+=1
    return prod


def my_pow1(num1,num2):
    return num1**num2

base=int(input("enter the base\n"))
exponent=int(input("enter the exponent\n"))

print(my_pow(base,exponent))
