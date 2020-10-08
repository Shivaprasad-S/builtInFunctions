def my_length(word):
    leng=0
    #lst=list(word)
    for _ in word:
        leng+=1
    return leng

string=str(input("enter a string\n"))
print(my_length(string))