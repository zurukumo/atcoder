N = int(input())

# 1000くらいまで素数を作る
prime = [2, 3]
ret = []
for i in range(5, 55555 + 1, 2):
    j = 0
    flg = False
    while prime[j] * prime[j] <= i:
        if i % prime[j] == 0:
            flg = True
            break
        j += 1
    if flg:
        continue
    prime.append(i)
    if i % 10 == 1:
        ret.append(i)
        if len(ret) == N:
            break

print(*ret)
