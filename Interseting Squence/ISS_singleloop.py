def gcd(x,y):
    if(y==0):
        return x
    return gcd(y,x%y)
try:
    T=int(input())
except:
    print("No. of test case must be intezer")
    exit()

while(T):
    T-=1
    try:
        k=int(input())

    except:
        print("Please enter a number")
        T+=1
        continue

    sum=0
    for i in range(1,((2*k)+1)):

        sum+=gcd((k+(i**2)),(k+((i+1)**2)))
    print(sum)