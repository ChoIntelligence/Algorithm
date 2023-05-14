n = int(input())
result = list(range(n))
for i in range(n) :
    a = list(map(int, input().split()))
    avg = sum(a[1:]) / a[0]
    count = 0
    for j in range(a[0]) :
        if a[j+1] > avg :
            count += 1
    result[i] = count / a[0] * 100

    
for i in range(n) :
    print("{0:0.3f}%".format(result[i]))
