N, M = map(int, input().split())

s = 0
for i in range(M + 1):
    s += pow(N, i)
    if s > 10**9:
        print("inf")
        exit()

print(s)
