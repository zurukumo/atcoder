N = int(input())
L = [int(i) for i in input().split()]

ret = 0
for i in range(N) :
  for j in range(i + 1, N) :
    for k in range(j + 1, N) :
      a, b, c = L[i], L[j], L[k]
      if a + b > c and b + c > a and c + a > b and a != b and b != c and c != a:
        ret += 1

print(ret)