N, K = map(int, input().split())
V = [int(i) for i in input().split()]

ans = 0

for left in range(0, K + 1) :
    for right in range(0, K - left + 1) :
        if left + right > N :
            break

        cd = K - left - right

        res = 0
        minus = []

        for vi in V[:left] :
            if vi < 0 :
                minus.append(vi)
            res += vi

        for vi in V[-1:-1-right:-1] :
            if vi < 0 :
                minus.append(vi)
            res += vi

        if len(minus) > cd :
            minus.sort()
            res -= sum(minus[:cd])
        else :
            res -= sum(minus)

        ans = max(ans, res)

print(ans)
            