A, B, C = map(int, input().split())

for a in range(A, A * 100 + 1, A) :
    if a % B == C :
        print('YES')
        break
else :
    print('NO')