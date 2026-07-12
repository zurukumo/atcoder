import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

T = int(input())
for _ in range(T):
    N = int(input())
    P = [int(i) for i in input().split()]

    bucket = [[p] for p in P]
    while len(bucket) > 1:
        new_bucket = []
        for i in range(0, len(bucket), 2):
            if bucket[i][0] > bucket[i + 1][0]:
                new_bucket.append(bucket[i + 1] + bucket[i])
            else:
                new_bucket.append(bucket[i] + bucket[i + 1])
        bucket = new_bucket

    print(*bucket[0])
