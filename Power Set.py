def int_to_binary(n):
    s=[]
    while(n!=0):
        if(n%2==1):
            s.append('1')
        else:
            s.append('0')
        n=n//2
    return s
a=list(map(int,input().split()))
n=2**len(a)
list2d=[]

for i in range(n):
    s=int_to_binary(i)
    row = []
    for j in range(len(s)):
        if(s[j]=='1'):
            row.append(a[j])
    list2d.append(row)
for row in list2d:
    print(row)


