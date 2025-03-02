T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    c = 2 ** bin(N)[2:].count("0")
    if c < K:
        print(-1)
    else:
        K -= 1
        for i in range(40):
            if (1 << i) & N == 0:
                N |= (K & 1) << i
                K >>= 1
        print(N)
