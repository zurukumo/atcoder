N = int(input())
ret = 0
for _ in range(N):
    l, r = map(int, input().split())
    ret += r - l + 1
print(ret)
