import bisect

N, Q = map(int, input().split())
S = input()

sum_one = []
cnt = 0
for c in S:
    if c == "1":
        cnt += 1
    sum_one.append(cnt)

cnt = 0
sum_two = []
for c in S[::-1]:
    if c == "2":
        cnt += 1
    sum_two.append(cnt)

sum_two = sum_two[::-1]

slashes = []
one_slashes = []
two_slashes = []
for i, c in enumerate(S):
    if c == "/":
        slashes.append(i)
        one_slashes.append(sum_one[i])
        two_slashes.append(sum_two[i])

for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1

    if L == 0:
        remove_one = 0
    else:
        remove_one = sum_one[L - 1]

    if R == N - 1:
        remove_two = 0
    else:
        remove_two = sum_two[R + 1]

    ok = 0
    ng = N + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        i = bisect.bisect_left(one_slashes, remove_one + mid)
        if 0 <= i < len(one_slashes) and two_slashes[i] >= remove_two + mid:
            ok = mid
        else:
            ng = mid

    if ok == 0:
        i = bisect.bisect_left(slashes, L)
        if i < len(slashes) and slashes[i] <= R:
            print(1)
        else:
            print(0)
    else:
        print(2 * ok + 1)
