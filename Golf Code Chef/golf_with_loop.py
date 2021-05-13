import sys
from itertools import chain

def get_ints():
    return map(int, sys.stdin.readline().strip().split())


T=int(input())#no of test case
while(T):
    N, x, k =  get_ints()
    str="NO"
    for i in chain(range(0,N+2,k),range(N+1, -1, -k)):
        if (i == x):
            str = "YES"
        else:
            continue
    print(str)
    T-=1

