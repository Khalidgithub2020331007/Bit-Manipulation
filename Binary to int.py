def ConvertToInt(s):
    p2=1
    num=0
    l=len(s)
    for i in range(l-1,-1,-1):
        if(s[i]=='1'):
            num+=p2
        p2*=2
    return num

s=input()
a=ConvertToInt(s);
print(a)