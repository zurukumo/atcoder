N = int(input())

ans = 0

for i in range(1, 10) :
    for j in range(1, 10) :
        ans += i * j

ans -= N

for i in range(1, 10) :
    if ans % i == 0 and ans <= i * 9:
        print('{} x {}'.format(i, ans // i))