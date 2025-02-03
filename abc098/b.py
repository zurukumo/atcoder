N = int(input())
S = input()

ret = 0
for i in range(N + 1):
    a = set(S[:i])
    b = set(S[i:])
    ret = max(ret, len(a & b))
print(ret)
