#project of delcte space in ends of strings
def del_space_string(string):
    index=None
    i=len(string)
    while(i>0):
        if string[i-1] != " ":
            index=i
            break
        i-=1
    new_string=string[:index]
    return new_string
