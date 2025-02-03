N, M = map(int, input().split())
A = [[1, int(i)] for i in input().split()]
BC = A + [[int(i) for i in input().split()] for _ in range(M)]

BC.sort(key=lambda x: x[1], reverse=True)

i = 0
res = 0

for B, C in BC :
    if i + B <= N :
        res += C * B
        i += B
    else :
        res += C * (N - i)
        break

print(res)
