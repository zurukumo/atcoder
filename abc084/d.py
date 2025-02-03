from bisect import bisect_left

Q = int(input())

prime = [2, 3]
for i in range(5, 10**5 + 1, 2):
    flg = True
    for p in prime:
        if p * p > i:
            break
        if i % p == 0:
            flg = False
            break
    if flg:
        prime.append(i)

like2017 = []
for p in prime:
    if (p + 1) // 2 in prime:
        like2017.append(p)

for _ in range(Q):
    l, r = map(int, input().split())
    print(bisect_left(like2017, r + 1) - bisect_left(like2017, l))
