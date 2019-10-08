from bisect import bisect_left

N = int(input())
A = [int(i) for i in input().split()]

s = sum(A)
for i in range(1, N) :
    A[i] += A[i-1]


def check(d) :
    ifr = bisect_left(A, (s - 3 * d) // 4)
    ito = bisect_left(A, (s + 3 * d) // 4)
    for i in range(ifr, min(N, ito + 1)) :
        jfr = bisect_left(A, A[i] + (s - A[i] - 2 * d) // 3)
        jto = bisect_left(A, A[i] + (s - A[i] + 2 * d) // 3)
        for j in range(max(i + 1, jfr), min(N, jto + 1)) :
            kfr = bisect_left(A, A[j] + (s - A[j] - d) // 2)
            kto = bisect_left(A, A[j] + (s - A[j] + d) // 2)
            for k in range(max(j + 1, kfr), min(N - 1, kto + 1)) :
                cut = [A[i], A[j] - A[i], A[k] - A[j], s - A[k]]
                if max(cut) - min(cut) <= d :
                    return True
    return False

ng, ok = 0, s
while ok - ng > 1 :
    mid = (ng + ok) // 2
    
    if check(mid) :
        ok = mid
    else :
        ng = mid

print(ok)