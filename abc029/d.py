N = int(input())

ret = 0
for i in range(1, 10) :
    # 取れるだけ取る
    ret += (N // (10**i)) * (10**(i-1))
    # 例えば10の位に注目する
    # N%100=19~99のとき10の位が1になるのは10~19の10個
    if N % (10**i) >= 2 * (10**(i-1)) - 1 :
        ret += 10**(i-1)
    # N%100=10~19のとき10の位が1になるのは10~N%100の(N%100-10+1)個
    elif N % (10**i) >= 10**(i-1) :
        ret += N % (10**i) - 10**(i-1) + 1
print(ret)