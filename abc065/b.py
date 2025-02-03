import sys

input = sys.stdin.readline

N = int(input())
a = [int(input()) - 1 for _ in range(N)]

pushed = [False] * N
now = 0
ret = 0
while True:
    if pushed[now]:
        print(-1)
        break
    if now == 1:
        print(ret)
        break
    pushed[now] = True
    now = a[now]
    ret += 1
