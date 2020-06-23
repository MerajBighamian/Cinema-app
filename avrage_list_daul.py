def sum_list(my_list):
    total=0
    counter=0
    for i in range(0,len(my_list)):
        counter+=len(my_list[i])
        for j in range(0,len(my_list[i])):
           total+=my_list[i][j]
    avg=total/counter
    return avg
