S = [input() for _ in range(12)]

ret = 0
for s in S :
    if 'r' in s :
        ret += 1
print(ret)