A = int(input())
B = int(input())

ret = set([1, 2, 3])
ret.remove(A)
ret.remove(B)
print(*ret)
