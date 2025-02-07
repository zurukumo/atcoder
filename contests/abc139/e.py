from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
A = [deque([int(i) - 1 for i in input().split()]) for _ in range(N)]


def solve():
    q = list(range(N))
    count = 0
    ret = 0
    while count != N * (N - 1):
        if len(q) == 0:
            return -1

        schedule = set()
        for i in q:
            j = A[i][0]
            if i in schedule or j in schedule:
                continue

            if i == A[j][0]:
                schedule.add(i)
                schedule.add(j)

        ret += 1
        q = []
        for i in schedule:
            A[i].popleft()
            if len(A[i]) > 0:
                q.append(i)
        count += len(schedule)

    return ret


print(solve())
