a, b, c = map(int, input().split())
list_ = [a, b, c]

if a == b :
    if b == c :
        print(10000 + a * 1000)
    else :
        print(1000 + a * 100)
elif b == c :
    print(1000 + b * 100)
elif a == c :
    print(1000 + 100 * a)
else :
    print(max(list_) * 100)
