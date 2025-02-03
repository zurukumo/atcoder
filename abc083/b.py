N, A, B = map(int, input().split())

ret = 0
for i in range(1, N + 1):
    if A <= sum(map(int, str(i))) <= B:
        ret += i
print(ret)
