def reverse_str_v1(s):
    r=''
    for char in s:
        r=char+r
    print("\n",r)
s=input("give a string:\n")
reverse_str_v1(s)

#-------------------------
def reverse_str_v2(s):
    r=''
    for i in range(len(s)-1,-1,-1):
            r=r+s[i]
    print(r)