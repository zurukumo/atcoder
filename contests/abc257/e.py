N = int(input())
C = [int(i) for i in input().split()]

ret = []
mod = N % min(C)

while N >= min(C):
    for i in range(8, -1, -1):
        if C[i] - min(C) <= mod:
            ret.append(str(i + 1))
            N -= C[i]
            mod -= C[i] - min(C)
            break

print("".join(ret))
