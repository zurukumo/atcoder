N = int(input())
H = [int(i) for i in input().split()]

for i in range(1, N):
    if H[i] > H[0]:
        print(i + 1)
        break
else:
    print(-1)
