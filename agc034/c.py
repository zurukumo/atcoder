N, X = map(int, input().split())
blu = [[int(i) for i in input().split()] for _ in range(N)]

b_total = 0
dblu = []
for b, l, u in blu :
    dblu.append((u*X-(u-l)*b, b, l, u))
    b_total += b * l
dblu.sort(reverse=True)

s = [0] * (N + 1)
for i in range(1, N + 1) :
    s[i] = s[i-1] + dblu[i-1][0]

ret = float('inf')

def judge(mid) :
    q = mid // X
    r = mid % X
    for i in range(N) :
        d, b, l, u = dblu[i]

        if q < i :
            tmp = s[q]
        else :
            tmp = s[q+1] - d

        if r < b :
            tmp += r * l
        else :
            tmp += b * l + u * (r - b)

        if tmp >= b_total :
            return True
    return False

left, right = -1, N * X

while right - left > 1 :
    mid = (left + right) // 2
    
    if judge(mid) :
        right = mid
    else :
        left = mid

print(right)