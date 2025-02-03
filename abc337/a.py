N = int(input())
XY = [[int(i) for i in input().split()] for _ in range(N)]

t = sum(x for x, y in XY)
a = sum(y for x, y in XY)
if t == a:
    print("Draw")
elif t > a:
    print("Takahashi")
else:
    print("Aoki")
