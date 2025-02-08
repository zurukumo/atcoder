
N = int(input())
a = [int(i) for i in input().split()]

ret = 0

pre = a[0]
count = 1
for i in range(1, N):
    if a[i] > pre:
        count += 1
    else:
        ret += count * (count + 1) // 2
        count = 1
    pre = a[i]

ret += count * (count + 1) // 2

print(ret)
