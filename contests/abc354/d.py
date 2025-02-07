A, B, C, D = map(int, input().split())

ymod0 = (D - 1) // 2 - (B - 1) // 2
ymod1 = (D - 2) // 2 - (B - 2) // 2
xmod0 = (C - 1) // 4 - (A - 1) // 4
xmod1 = (C - 2) // 4 - (A - 2) // 4
xmod2 = (C - 3) // 4 - (A - 3) // 4
xmod3 = (C - 4) // 4 - (A - 4) // 4

ret = 0
ret += (ymod0 * xmod0 + ymod1 * xmod1) * 2
ret += (ymod1 * xmod0 + ymod0 * xmod1 + ymod1 * xmod2 + ymod0 * xmod3) * 1

print(ret)
