N, A, B, C = map(int, input().split())
s = [[ord(i) - ord("A") for i in input()] for _ in range(N)]

L = [A, B, C]
ret = []
for i in range(N):
    x, y = s[i]
    done = False
    if L[x] + 1 >= 0 and L[y] - 1 >= 0:
        L[x] += 1
        L[y] -= 1
        if i + 1 != len(s):
            u, v = s[i + 1]
            if (L[u] + 1 >= 0 and L[v] - 1 >= 0) or (L[u] - 1 >= 0 and L[v] + 1 >= 0):
                done = True
                ret.append(x)
        else:
            done = True
            ret.append(x)
        if not done:
            L[x] -= 1
            L[y] += 1

    if not done and L[x] - 1 >= 0 and L[y] + 1 >= 0:
        L[x] -= 1
        L[y] += 1
        if i + 1 != len(s):
            u, v = s[i + 1]
            if (L[u] - 1 >= 0 and L[v] + 1 >= 0) or (L[u] + 1 >= 0 and L[v] - 1 >= 0):
                done = True
                ret.append(y)
        else:
            done = True
            ret.append(y)
        if not done:
            L[x] += 1
            L[y] -= 1

    if not done:
        print("No")
        break
else:
    print("Yes")
    for r in ret:
        print(chr(ord("A") + r))
