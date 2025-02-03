A, B = map(int, input().split())

ret = 0
for i in range(A, B + 1):
    if str(i) == str(i)[::-1]:
        ret += 1
print(ret)
