N, K = map(int, input().split())
S = input()

ma, mb = (1 << 61) - 1, (1 << 31) - 1
wa, wb = 0, 0
mem = dict()
for i in range(N):
    wa += pow(26, ord(S[i]) - 97, ma)
    wb += pow(26, ord(S[i]) - 97, mb)
    wa %= ma
    wb %= mb

    if i >= K - 1:
        if (wa, wb) in mem and i - mem[(wa, wb)] >= K:
            print("YES")
            break

        if not (wa, wb) in mem:
            mem[(wa, wb)] = i

        wa -= pow(26, ord(S[i - K + 1]) - 97, ma)
        wb -= pow(26, ord(S[i - K + 1]) - 97, mb)

else:
    print("NO")
