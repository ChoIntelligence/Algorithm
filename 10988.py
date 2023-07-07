s = input()
c = 0
for i in range(int(len(s) / 2)) :
    if s[i] != s[-i-1] :
        c += 1

if c == 0 :
    print(1)
else :
    print(0)
