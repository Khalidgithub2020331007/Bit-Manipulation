a=list(map(int,input().split()))
b=a[0]
for i in range(1,len(a)):
    b=b^a[i]
print('The single number is',b)