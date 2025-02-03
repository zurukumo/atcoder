L = int(input())

bunsi = 1
bunbo = 1
for i in range(1, 11 + 1):
  bunsi *= L - i
  bunbo *= i

print(bunsi // bunbo)
  