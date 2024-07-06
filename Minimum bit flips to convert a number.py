def count_set(n):
    cnt=0
    while(n>0):
        n=n&n-1
        cnt+=1
    return cnt;
start,goal=map(int,input().split())
xor_value=start^goal
print(count_set(xor_value))