def xor_from_1_to_n(n):
    if(n%4==1):
        return 1
    if(n%4==2):
        return n+1
    if(n%4==3):
        return 0
    else:
        return n

def xor_from_l_to_r(l,r):
    return xor_from_1_to_n(l-1)^xor_from_1_to_n(r)
l,r=map(int,input().split())
ans=xor_from_l_to_r(l,r)
print(ans)