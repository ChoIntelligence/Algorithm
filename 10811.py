import sys
n, m = map(int, sys.stdin.readline().split())
a = list(range(1, n + 1))

for k in range(m) :
    i, j = map(int, sys.stdin.readline().split())
    temp = a[i-1:j]
    temp.reverse()
    a[i-1:j] = temp

for i in range(n) :
    print(a[i], end = ' ')
