A, B = input().split()
sum = 0
m = 1
for i in A :
    sum += int(i) * m
    m *= 10
x = sum
sum = 0
m = 1

for i in B :
    sum += int(i) * m
    m *= 10
y = sum

if x > y :
    print(x)
else :
    print(y)
