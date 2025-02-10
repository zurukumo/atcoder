T = int(input())

mod = 998244353

for _ in range(T):
    N = int(input())
    S = input()

    ret = 0
    length = (N + 1) // 2
    for i in range(length):
        ret += (ord(S[i]) - ord("A")) * pow(26, length - i - 1, mod)
    if S[N // 2 - 1 :: -1] <= S[-(N // 2) :]:
        ret += 1

    print(ret % mod)
