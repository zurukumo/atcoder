def solve(A):
    if sum(A) == 0:
        return "Bob"

    A.append(0)
    cnt = 0
    for a in A:
        if a == 1:
            cnt += 1
        elif a == 0:
            if cnt != 0 and cnt != 2:
                return "Alice"
            cnt = 0

    return "Bob"


T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(i) for i in input().split()]
    print(solve(A))
