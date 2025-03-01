T = int(input())
for _ in range(T):
    N, X, Y = input().split()
    X += "C"
    Y += "C"

    flag = True
    xa, xc = 0, 0
    for x, y in zip(X, Y):
        if x != "C" and y == "C":
            flag = False
            break

        if x == y == "C":
            if xa != 0:
                flag = False
                break
            xa, xc = 0, 0
            continue

        if x == "A":
            xa += 1
        elif x == "C":
            xc += 1

        if y == "A":
            if xa > 0:
                xa -= 1
            elif xc > 0:
                xc -= 1
            else:
                flag = False
                break

    print("Yes" if flag else "No")
