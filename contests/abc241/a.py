a = [int(i) for i in input().split()]

cur = 0
for _ in range(3):
    cur = a[cur]
print(cur)
