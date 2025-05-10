import collections
import heapq

N = int(input())
rcx = [[int(i) for i in input().split()] for _ in range(N)]

rsum = collections.defaultdict(int)
csum = collections.defaultdict(int)
points = dict()

for r, c, x in rcx:
    rsum[r] += x
    csum[c] += x
    points[(r, c)] = x

rs = sorted(rsum.items(), key=lambda x: x[1], reverse=True)
cs = sorted(csum.items(), key=lambda x: x[1], reverse=True)

hq = [(-(rs[0][1] + cs[0][1]), 0, 0)]
visited = set()
visited.add((0, 0))
ret = 0
while hq and N + 10 >= 0:
    _, ri, ci = heapq.heappop(hq)
    if (rs[ri][0], cs[ci][0]) in points:
        ret = max(ret, rs[ri][1] + cs[ci][1] - points[(rs[ri][0], cs[ci][0])])
    else:
        ret = max(ret, rs[ri][1] + cs[ci][1])
    N -= 1
    if ri + 1 < len(rs) and (ri + 1, ci) not in visited:
        heapq.heappush(hq, (-(rs[ri + 1][1] + cs[ci][1]), ri + 1, ci))
        visited.add((ri + 1, ci))
    if ci + 1 < len(cs):
        heapq.heappush(hq, (-(rs[ri][1] + cs[ci + 1][1]), ri, ci + 1))
        visited.add((ri, ci + 1))

print(ret)
