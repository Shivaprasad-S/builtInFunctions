def myabs(number):
    """ Implementation of built-in `abs` function """
    return -number if number<0 else number


def myall(iterable):
    """ Implementation of built-in `all` function """
    for item in iterable:
        if not item:
            return False
    return True



def myany(iterable):
    """ Implementation of built-in `any` function """
    for item in iterable:
        if item:
            return True
    return False


def mylen(s):
    """ Implementation of built-in `len` function """
    length=0
    for _ in s:
        length+=1
    return length


def mysum(iterable):
    """ Implementation of built-in `sum` function """
    sum=0
    for item in range(len(iterable)):
        sum=sum+iterable[item]
    return sum


def mymax(iterable):
    """ Implementation of built-in `max` function """
    maximum=iterable[0]
    for item in range(1,len(iterable)):
        if iterable[item]>maximum:
            maximum=iterable[item]
    return maximum


def mymin(iterable):
    """ Implementation of built-in `min` function """
    minimum=iterable[0]
    for item in range(1,len(iterable)):
        if iterable[item]<minimum:
            minimum=iterable[item]
    return minimum


def mydivmod(num1, num2):
    """ Implementation of built-in `divmod` function """
    return (num1//num2,num1%num2)


def mybool(x):
    """ Implementation of built-in `bool` function """
    return True if x else False


def mypow(base, exp):
    """ Implementation of built-in `pow` function """
    counter=1
    prod=1
    while counter<=exp:
        prod=prod*base
        counter+=1
    return prod


def myreversed(seq):
    """ Implementation of built-in `reversed` function """
    reverse=seq[::-1]
    return reverse


def myenumerate(iterable, start=0):
    """ Implementation of built-in `enumerate` function """
    lst=[]
    for i in range(len(iterable)):
        lst.append((i,iterable[i]))
    return(lst)


def mybin(x):
    """ Implementation of built-in `bin` function """
    lst=['0b']
    while(x>0):
        r=x%2
        x=x//2
        lst.insert(1,str(r))
    return "".join(lst)


def myhex(x):
    """ Implementation of built-in `hex` function """
    lst=['0x']
    while(x>0):
        r=x%16
        x=x//16
        if r==10:
            r='a'
        elif r==11:
            r='b'
        elif r==12:
            r='c'
        elif r==13:
            r='d'
        elif r==14:
            r='e'
        elif r==15:
            r='f'
        else:
            r=r
        lst.insert(1,str(r))
    return ''.join(lst)

def myoct(x):
    """ Implementation of built-in `oct` function """
    lst=['0o']
    while(x>0):
        r=x%8
        x=x//8
        lst.insert(1,str(r))
    return "".join(lst)

def myisinstance(object, classinfo):
    """ Implementation of built-in `isinstance` function """
    t1=type(object)
    t2=str(t1).find(classinfo)
    if t2>=0:
        return True
    return False


def myround(number, ndigits=None):
    """ Implementation of built-in `round` function """
    dot='.'
    number=str(number)
    lst=list(str(number))
    decimal=str(number).find(dot)
    if decimal<0:
        return number
    else:
        if int(len(number[(decimal+1):]))<=ndigits:
            return number
        else:
            lastdigit=decimal+ndigits+1
            if int(lst[lastdigit])>5:
                lst[lastdigit-1]=str(int(lst[lastdigit-1])+1)
            return ''.join(lst[0:lastdigit])


def mysorted(iterable, reverse=False):
    """ Implementation of built-in `sorted` function """
    iterable=list(iterable)
    #print(len(lst))
    for i in range(len(iterable)):
        for j in range(len(iterable)):
            if i!=j:
                if iterable[i]>iterable[j]:
                    temp=iterable[i]
                    iterable[i]=iterable[j]
                    iterable[j]=temp
    return iterable