N = int(input())
X = int(input())
sum = 0
for i in range(N, -1, -1) :
    sum += X // (10 ** i)
    X = X % (10 ** i)
print(sum)
