N, D, P = map(int, input().split())
F = [int(i) for i in input().split()]

F.sort()

ret = 0
tmp_s = 0
tmp_c = 0
while F:
    f = F.pop()
    tmp_s += f
    tmp_c += 1

    if tmp_c >= D:
        ret += min(tmp_s, P)
        tmp_s = 0
        tmp_c = 0

ret += min(tmp_s, P)
print(ret)
