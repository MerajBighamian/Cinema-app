#find_mismatch in double string
def find_mismatch(str1,str2):
    #counter for count mismatchs in double string
    counter_mismatch=0
    str1=str1.lower()
    str2=str2.lower()
    #copy of str2 for check in line 24 and 26 
    str3=str2.lower()
    #iterate on str1
    for i in str1:
        #valid was False
        valid=False
        #iterate on str2
        for j in str2:
            #check if i(character of str1) == j(character of str2)
            if i==j:
                #valid = True
                valid=True
                #delete character matched for not repete and use in next loop  
                str2=str2.replace(j,"",1)
                #break for loop line 14
                break
        #Is valid False
        if valid==False:
            #if valid is False counter_mismatch+1
            counter_mismatch+=1
    #check for matched compelete str1 and str2
    if str1==str3:
        return 0
    #check Is counter_mismatch=1  and length str1 equal of length str3(copy of str 2)
    elif len(str1)==len(str3) and counter_mismatch==1:
        return 1
    #run if counter_mismatch>1 
    else:
        return 2
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # for char in str1:
    #     print("char is  ----------------->",char)
    #     if str1 in str2:
    #         str2=str2.replace(str1," ")
    #         print("str2 is ------------------------->",str2)
    #     else:
    #         count_mismatch+=1
    #         print("count_mismatch is  ----------------->",count_mismatch)
    # if str1==str2:
    #     return 0
    # elif len(str1)==len(str2) and count_mismatch==1:
    #     return 1
    
    
    # elif len(str1)<len(str2):
    #     for i in range(0,len(str1)):
    #         if str1[i] != str2[i]:
    #             count_mismatch+=1
    #             if count_mismatch>1:
    #                 return 2
    #                 break
    
        
    # elif len(str1)==len(str2):
    #     for i in range(0,len(str1)):
    #         if str1[i] != str2[i]:
    #             count_mismatch+=1
    #             if count_mismatch==1:
    #                 return 1
    #                 break
    
    # elif len(str1)>len(str2):
    #     for i in range(0,len(str2)):
    #         if str1[i] != str2[i]:
    #             count_mismatch+=1
    #             if count_mismatch>1:
    #                 return 2
    #                 break
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # for i in str1:
    #     if i in str2:
    #         count_mismatch+1
    # if str1==str2:
    #     return 0
    
    # elif len(str1) == len(str2) and count_mismatch==1:
    #     return 1
    
    # else:
    #     return 2
        
