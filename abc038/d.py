from bisect import bisect_left

N = int(input())
wh = []

for _ in range(N):
    w, h = map(int, input().split())
    wh.append([w, h])

wh.sort(key=lambda x: x[1], reverse=True)
wh.sort(key=lambda x: x[0])
wh = [h for w, h in wh]

lis = [wh[0]]
for i in range(1, N):
    seq = wh[i]
    if seq > lis[-1]:
        lis.append(seq)
    else:
        lis[bisect_left(lis, seq)] = seq

print(len(lis))
