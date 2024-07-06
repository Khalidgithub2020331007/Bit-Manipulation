def xor_from_1_to_n(n):
    if(n%4==1):
        return 1
    if(n%4==2):
        return n+1
    if(n%4==3):
        return 0
    else:
        return n


n=int(input())
ans=xor_from_1_to_n(n)
print(ans)

