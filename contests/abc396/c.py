N, M = map(int, input().split())
B = [int(i) for i in input().split()]
W = [int(i) for i in input().split()]

B.sort()
W.sort()
ret = 0
b = 0
w = 0
while B and B[-1] >= 0:
    ret += B.pop()
    b += 1
while W and W[-1] >= 0 and w < b:
    ret += W.pop()
    w += 1
while w == b and B and W and B[-1] + W[-1] >= 0:
    ret += B.pop() + W.pop()

print(ret)
