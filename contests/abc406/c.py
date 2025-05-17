N = int(input())
P = [int(i) for i in input().split()]

ret = 0

N += 1
P.append(-float("inf"))

pre_up = 0
now_up = 0
i = 0
while i < N:
    if P[i - 1] < P[i]:
        now_up += 1
        i += 1
    else:
        ret += max(0, (pre_up - 1) * (now_up - 1))
        pre_up, now_up = now_up, 1
        while i < N and P[i - 1] > P[i]:
            i += 1

print(ret)
