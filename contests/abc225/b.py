N = int(input())
ab = [[int(i) - 1 for i in input().split()] for _ in range(N - 1)]

e = [0] * N
for a, b in ab:
    e[a] += 1
    e[b] += 1

if N - 1 in e:
    print("Yes")
else:
    print("No")
