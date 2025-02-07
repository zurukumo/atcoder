x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

if x2 <= x1 - r and x1 + r <= x3 and y2 <= y1 - r and y1 + r <= y3:
    red = "NO"
else:
    red = "YES"

M = 0
for x, y in ((x2, y2), (x2, y3), (x3, y2), (x3, y3)):
    M = max(M, (x - x1) ** 2 + (y - y1) ** 2)

if M <= r**2:
    blue = "NO"
else:
    blue = "YES"

print(red)
print(blue)
