import sys
t = int(sys.stdin.readline())
for i in range(t) :
    a, b = map(int, sys.stdin.readline().split())
    print('Case #{0}: {1} + {2} = {3}'.format(i + 1, a, b, a + b))