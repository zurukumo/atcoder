N, H, X = map(int, input().split())
P = [int(i) for i in input().split()]

for i in range(N):
    if H + P[i] >= X:
        print(i + 1)
        break
