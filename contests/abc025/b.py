N, A, B = map(int, input().split())

ret = 0
for _ in range(N):
    s, d = input().split()
    d = int(d)
    if d < A:
        d = A
    elif d > B:
        d = B

    if s == "East":
        ret += int(d)
    else:
        ret -= int(d)

if ret > 0:
    print("East", ret)
elif ret < 0:
    print("West", -ret)
else:
    print(0)
