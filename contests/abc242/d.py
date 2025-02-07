S = input()
Q = int(input())
tk = [[int(i) for i in input().split()] for _ in range(Q)]


for t, k in tk:
    k -= 1
    diff = 0
    while t != 0 and k != 0:
        if k % 2 == 0:
            diff += 1
        else:
            diff += 2
        t = t - 1
        k = k // 2

    if t != 0:
        diff += t

    base = ord(S[k]) - ord("A")
    print(chr(ord("A") + (base + diff) % 3))
