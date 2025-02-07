N = int(input())
A = [int(i) for i in input().split()]

k, v = 0, -1
for i in range(2, 1000):
    cnt = 0
    for a in A:
        if a % i == 0:
            cnt += 1

    if cnt > v:
        k, v = i, cnt

print(k)
