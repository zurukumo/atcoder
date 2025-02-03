Q = int(input())
AB = [[int(i) for i in input().split()] for _ in range(Q)]
for a, b in AB :
    ret = 0
    sqrt = int((a * b) ** 0.5)
    ret += sqrt - 1
    ret += (a * b - 1) // sqrt - 1
    if a == b :
        ret += 1
    print(ret)