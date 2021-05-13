def power(x, y, p):
    res = 1
    x = x % p
    if (x == 0):
        return 0

    while (y > 0):

        # If y is odd, multiply
        # x with result
        #if((y%2==1)
        if((y & 1)==1):
            res=(res*x)%p
        #y=y/2
        y=y>>1
        #y must be even
        x=(x*x)%p

    return res

T = int(input())
while (T):
    T -= 1
    N = int(input())
    p=10**9+7
    ans=power(2,N-1,p)
    print(ans)