N = int(input())
a = [int(i) for i in input().split()]

b = [(v, k) for k, v in enumerate(a)]
b.sort(reverse=True)

for i in range(N):
    print(b[i][1] + 1)
