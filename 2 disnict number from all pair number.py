def find(a):
    xorr=0

    for i in range(len(a)):
        xorr=xorr^a[i]
    rightmost=xorr^(xorr&(xorr-1))
    b1=0
    b2=0
    for i in range(len(a)):
        if(a[i]&rightmost):
            b1=b1^a[i]
        else:
            b2=b2^a[i]
    print(b1,b2)
a=list(map(int,input().split()))
find(a)