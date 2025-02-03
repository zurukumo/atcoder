X = int(input())

ans = 0
while X >= 500:
    X -= 500
    ans += 1000

while X >= 5:
    X -= 5
    ans += 5

print(ans)
