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
    a=[]
    for i in range(1,(2*k)+2):
        a.append(k+(i**2))

    b=[]
    for j in range(len(a)-1):
        b.append(gcd(a[j],a[j+1]))
    print(sum(b))

