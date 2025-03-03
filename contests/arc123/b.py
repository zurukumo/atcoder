N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
ret = 0
while A and B and C:
    if not A[-1] < B[-1]:
        B.pop()
        continue
    if not B[-1] < C[-1]:
        C.pop()
        continue

    A.pop()
    B.pop()
    C.pop()
    ret += 1
print(ret)
