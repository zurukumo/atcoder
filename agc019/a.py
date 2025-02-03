Q, H, S, D = map(int, input().split())
N = int(input()) * 4

order = [(Q, 1), (H, 2), (S, 4), (D, 8)]
order.sort(key=lambda x: x[0] / x[1])

ret = 0
for i in range(4) :
  ret += (N // order[i][1]) * order[i][0]
  N %= order[i][1]
  
print(ret)