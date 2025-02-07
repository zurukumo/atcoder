N = int(input())
a = [int(i) for i in input().split()]

ret = 0
for a_ in a:
    while a_ % 2 == 0:
        a_ //= 2
        ret += 1

print(ret)
