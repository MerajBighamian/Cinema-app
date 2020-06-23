def find_max(lists):
    if len(lists)>0:
        max_item=lists[0][0]
        result=False
        for i in lists:
           # print("i ----------------->",i)
            for j in i:
                #print("j ----------------->",j)
                if j%2==0:
                    if j>max_item:
                        max_item = j
                        #print("max ----------------->",max_item)
                        result=True
                        #print("result ----------------->",result)
        if result:
            return max_item
        else:
            return None
    else:
        return None
    