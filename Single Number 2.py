def single_number_found(a):
    ans=0

    for i in range(32):
        cnt=0
        for j in range(len(a)):
            if(a[j]&1<<i):
                cnt+=1
        if(cnt%3==1):
            ans=ans|(i<<i)
    return ans
a=list(map(int,input().split()))
n=single_number_found(a)
print(n)
