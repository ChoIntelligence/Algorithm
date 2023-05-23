a = list(range(28))

for i in range(28) :
    num = int(input())
    a[i] = num

for i in range(30) :
    if i + 1 not in a :
        print(i + 1)
