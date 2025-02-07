N = int(input())
XYZ = [[int(i) for i in input().split()] for _ in range(N)]

total_z = sum(z for x, y, z in XYZ)
dp = [float("inf")] * (total_z + 1)
dp[0] = 0
for x, y, z in XYZ:
    for i in range(total_z, -1, -1):
        if i - z < 0:
            continue

        half = (x + y) // 2 + 1
        if half - x > 0:
            dp[i] = min(dp[i], dp[i - z] + half - x)
        else:
            dp[i] = min(dp[i], dp[i - z])

print(min(dp[total_z // 2 + 1 :]))
