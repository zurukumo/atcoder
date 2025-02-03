N = int(input())
a = [int(i) for i in input().split()]

ret = 0
a.sort(reverse=True)
for i in range(1, 1 + 2 * N, 2) :
  ret += a[i]

print(ret)