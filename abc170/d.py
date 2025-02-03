N = int(input())
A = [int(i) for i in input().split()]

x = [0] * (10**6 + 10)
y = [0] * (10**6 + 10)
for a in A:
    x[a] = 1
    y[a] += 1

for i in range(10**6 + 1):
    if x[i] == 0:
        continue
    j = i * 2
    while j <= 10**6:
        x[j] = 0
        j += i

ret = 0
for i in range(10**6 + 1):
    if x[i] == 1 and y[i] == 1:
        ret += 1

print(ret)
