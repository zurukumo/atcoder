import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

H, W = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(H)]
B = [[int(i) for i in input().split()] for _ in range(H)]
C = [[abs(A[y][x] - B[y][x]) for x in range(W)] for y in range(H)]

N = 13000
half = N // 2

dp = [[0] * W for _ in range(H)]
dp[0][0] = (1 << (half - C[0][0])) | (1 << (half + C[0][0]))

for y in range(H) :
    for x in range(W) :
        if y != 0 :
            dp[y][x] |= (dp[y-1][x] >> C[y][x]) | (dp[y-1][x] << C[y][x])
                    
        if x != 0 :
            dp[y][x] |= (dp[y][x-1] >> C[y][x]) | (dp[y][x-1] << C[y][x])

b = bin(dp[-1][-1])[2:][::-1]
ret = float('inf')
for k, v in enumerate(b) :
    if v == '1' :
        ret = min(ret, abs(k - half))
        
print(ret)