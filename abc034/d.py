N, K = map(int, input().split())
wp = [[int(i) for i in input().split()] for _ in range(N)]

limit = 0

left, right = 0, 100
while limit < 100:
    mid = (left + right) / 2
    l = [w * (p - mid) for w, p in wp]
    l.sort(reverse=True)

    if sum(l[:K]) >= 0:
        left = mid
    else:
        right = mid

    limit += 1

print(left)
