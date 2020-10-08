def my_any(data):
    for item in data:
        if item:
            return True
    return False

mylist=[2,4,"xyz",[1,2],{"a":1,"b":2}]
mylist1=[0,0j,None,{},[]]
print(my_any(mylist1))