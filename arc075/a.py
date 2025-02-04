import sys

input = sys.stdin.readline

N = int(input())
s = [int(input()) for _ in range(N)]

dp = {
    0,
}
for si in s:
    dp_ = set()
    for dpi in dp:
        dp_.add(dpi + si)
    dp = dp | dp_

dp = list(dp)
dp.sort(reverse=True)
for dpi in dp:
    if dpi % 10 != 0:
        print(dpi)
        break
else:
    print(0)
