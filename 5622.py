S = input()
sum = 0
for i in S :
    if (ord(i) >= ord('A') and ord(i) < ord('D')) :
        sum += 2
    elif (ord(i) >= ord('D') and ord(i) < ord('G')) :
        sum += 3
    elif (ord(i) >= ord('G') and ord(i) < ord('J')) :
        sum += 4
    elif (ord(i) >= ord('J') and ord(i) < ord('M')) :
        sum += 5
    elif (ord(i) >= ord('M') and ord(i) < ord('P')) :
        sum += 6
    elif (ord(i) >= ord('P') and ord(i) < ord('T')) :
        sum += 7
    elif (ord(i) >= ord('T') and ord(i) < ord('W')) :
        sum += 8
    elif (ord(i) >= ord('W') and ord(i) <= ord('Z')) :
        sum += 9
print(sum+len(S))
