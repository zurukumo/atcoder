N = int(input())
s = [int(i) for i in input().split()]

ret = 0
for c in range(1, N) :
    k = 1
    tmp = 0
    flag = (N - 1) % c == 0
    while c * k < N - 1 :
        l = c * k
        r = N - 1 - l

        if (flag and r <= l) or r <= c:
            break

        tmp += s[l] + s[r]
        ret = max(ret, tmp)
        k += 1

print(ret)
