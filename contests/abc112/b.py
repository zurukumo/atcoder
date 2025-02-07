N, T = map(int, input().split())
ct = [[int(i) for i in input().split()] for _ in range(N)]

ret = float("inf")
for c, t in ct:
    if t <= T:
        ret = min(ret, c)

if ret == float("inf"):
    print("TLE")
else:
    print(ret)
