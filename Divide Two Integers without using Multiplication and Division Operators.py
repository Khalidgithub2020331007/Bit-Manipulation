def xor_division(n,d):
    if(n==d): return 1;
    ans=0
    while(n>=d):
        cnt=0
        while(n>=(d<<(cnt+1))):
            cnt+=1
        ans+=1<<cnt
        n=n-d*(1<<cnt)
    return ans

while 1:
    n, d = map(int, input().split())
    ans = xor_division(n, d)
    print(ans)
