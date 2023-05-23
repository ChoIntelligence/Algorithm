import sys

n, m = map(int, sys.stdin.readline().split())
a = list(range(1, n + 1))
temp = 0

for k in range(m) :
    i, j = map(int, sys.stdin.readline().split())
    temp = a[i-1]
    a[i-1] = a[j-1]
    a[j-1] = temp

for k in range(n) :
    print(a[k], end = ' ')
