import sys

def get_ints():
    return map(int, sys.stdin.readline().strip().split())


T = int(input())  # no of test case
while (T):
    N, x, k = get_ints()
    T -= 1

    if (x % k == 0):
        print("YES")
        continue
    elif (((N + 1 - x) % k) == 0):
        print("YES")
        continue
    else:
        print("NO")
        continue
