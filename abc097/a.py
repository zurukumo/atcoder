a, b, c, d = map(int, input().split())

if abs(c - a) <= d or (abs(b - a) <= d and abs(b - c) <= d) :
    print('Yes')
else :
    print('No')