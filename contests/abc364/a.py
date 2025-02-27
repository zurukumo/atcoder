N = int(input())
S = [input() for _ in range(N)]

ret = 1
for i in range(1, N):
    ret += 1
    if S[i - 1] == "sweet" and S[i] == "sweet":
        break
print("Yes" if ret == len(S) else "No")
