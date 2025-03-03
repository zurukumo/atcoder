n = int(input())
R = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
q = int(input())
rc = [[int(i) for i in input().split()] for _ in range(q)]

ret = ""
for r, c in rc:
    rv = R[r - 1]
    cv = C[c - 1]
    if rv >= (n - cv + 1):
        ret += "#"
    else:
        ret += "."
print(ret)
