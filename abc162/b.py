N = int(input())

ans = 0
for i in range(N + 1):
    if not (i % 3 == 0 or i % 5 == 0):
        ans += i

print(ans)
