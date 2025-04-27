T = input()
U = input()

flag = False
for i in range(len(T) - len(U) + 1):
    for j in range(len(U)):
        if T[i + j] == U[j] or T[i + j] == "?":
            continue
        else:
            break
    else:
        flag = True
        break


if flag:
    print("Yes")
else:
    print("No")
