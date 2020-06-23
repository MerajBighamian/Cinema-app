def single_insert_or_delete(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    count_mismatch=0
    for i in s1:
        if i not in s2:
            print("----------->",i)
            count_mismatch+=1
            print("----------->",count_mismatch)
    if s1==s2:
            return 0
    elif (len(s1)<len(s2) or len(s1)>len(s2)) and count_mismatch==1:
        return 1
    else:
        return 2
    
    
