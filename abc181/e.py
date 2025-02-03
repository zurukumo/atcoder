from bisect import bisect_left, bisect_right

N, M = map(int, input().split())
H = [int(i) for i in input().split()]
W = [int(i) for i in input().split()]

H.sort()

l = []
r = []
for i in range(0, N - 1, 2) :
  l.append(H[i + 1] - H[i])
  r.append(H[i + 2] - H[i + 1])

for i in range(1, N // 2) :
  l[i] += l[i - 1]
  r[N//2 - 1 - i] += r[N//2 - i]
l = [0] + l
r = r + [0]

ret = float('inf')
for w in W :
  p = bisect_left(H, w)
  d = H[p - p % 2]
  ret = min(ret, r[p // 2] + l[p // 2] + abs(w - d))
  
print(ret)