N = int(input())
S = input()
T = input()

ret = 0
for i in range(N):
    if S[i] != T[i]:
        ret += 1

print(ret)
