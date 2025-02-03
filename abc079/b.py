N = int(input())

pre, cur = 2, 1
while N - 2 >= 0:
    pre, cur = cur, pre + cur
    N -= 1
print(cur)
