N = int(input())
W = [int(i) for i in input().split()]

ans = float('inf')
total = sum(W)

S1 = 0
for i in range(N):
    S1 += W[i]
    S2 = total - S1
    ans = min(ans, abs(S1 - S2))
    
    if S2 - S1 < 0:
        break

print(ans)