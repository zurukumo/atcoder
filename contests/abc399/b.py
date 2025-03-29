N = int(input())
P = [int(i) for i in input().split()]

for p in P:
    s = 0
    for q in P:
        if q > p:
            s += 1
    print(s + 1)
