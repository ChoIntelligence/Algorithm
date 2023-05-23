a = []
for i in range(10) :
    n = int(input())
    n %= 42
    if n not in a :
        a.append(n)

print(len(a))
