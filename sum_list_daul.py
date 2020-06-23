def sum_list(my_list):
    total=0
    for i in range(0,len(my_list)):
        for j in range(0,len(my_list[i])):
           total+=my_list[i][j]
           
    return total

