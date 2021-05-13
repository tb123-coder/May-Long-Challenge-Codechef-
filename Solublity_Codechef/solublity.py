T=int(input())#no of test case
while(T):
    X, A, B = [int(x) for x in input().split()]
    Sol=int(A+((100-X)*B))
    print(Sol*10)
    T-=1
