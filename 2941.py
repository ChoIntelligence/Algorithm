s = input()
count = len(s)

for i in range(len(s)) :
    if s[i:i+3] == 'dz=' :
        count -= 1
    elif s[i:i+2] == 'c=' or s[i:i+2] == 'c-' or s[i:i+2] == 'd-' or s[i:i+2] == 'lj' or s[i:i+2] == 'nj' or s[i:i+2] == 's=' or s[i:i+2] == 'z=' :
        count -= 1

print(count)
