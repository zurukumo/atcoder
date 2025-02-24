N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N)]

for i in range(N):
    AB[i][0], AB[i][1] = min(AB[i]), max(AB[i])

AB.sort()

ret = True
right = []
for a, b in AB:
    while right and a > right[-1]:
        right.pop()

    if right and b > right[-1]:
        ret = False
        break
    right.append(b)

print("No" if ret else "Yes")
