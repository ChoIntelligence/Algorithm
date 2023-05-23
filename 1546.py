import sys

n = int(input())

a = list(map(int, sys.stdin.readline().split()))

best = max(a)

for i in range(n) :
    a[i] = a[i]/best*100

print(sum(a)/len(a))
