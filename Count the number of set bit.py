n=int(input())
cnt=0
while(n>0):
    cnt+=n&1
    n=n>>1
print(cnt)