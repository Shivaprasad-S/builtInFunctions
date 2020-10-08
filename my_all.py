def my_all(data):
    for item in data:
        if not item:
            return False
    return True

mylist=[2,4,"xyz",[],{"a":1,"b":2}]
print(my_all(mylist))