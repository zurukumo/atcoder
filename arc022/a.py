S = input().upper()

flag = 0
for s in S:
    if flag == 0 and s == "I":
        flag = 1
    elif flag == 1 and s == "C":
        flag = 2
    elif flag == 2 and s == "T":
        print("YES")
        break
else:
    print("NO")
