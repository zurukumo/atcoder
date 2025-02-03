N = int(input())
S = [int(i) for i in input().split()]

ans = [0] * (N + 2)
for i in range(3, N + 2):
    ans[i] = S[i - 2] - S[i - 3] + ans[i - 3]

a1 = -min(a for a in ans[0::3])
a2 = -min(a for a in ans[1::3])
a3 = -min(a for a in ans[2::3])

if a1 + a2 + a3 <= S[0]:
    a1 += S[0] - a1 - a2 - a3
    for i in range(0, N + 2, 3):
        ans[i] += a1
    for i in range(1, N + 2, 3):
        ans[i] += a2
    for i in range(2, N + 2, 3):
        ans[i] += a3

    print("Yes")
    print(*ans)
else:
    print("No")
