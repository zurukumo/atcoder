N = int(input())
TA = [[int(i) for i in input().split()] for _ in range(N)]

T, A = TA[0]
for i in range(1, N):
    t, a = TA[i]
    if T / A < t / a:
        i = 0
        while (A + i) * t % a != 0:
            i += 1
        T = (A + i) * t // a
        A = A + i
    else:
        i = 0
        while (T + i) * a % t != 0:
            i += 1
        A = (T + i) * a // t
        T = T + i

print(T + A)
