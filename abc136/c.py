N = int(input())
H = [0] + [int(i) for i in input().split()]

flg = True
for i in range(1, N + 1):
    if H[i] != H[i - 1]:
        H[i] -= 1
    if H[i] < H[i - 1]:
        flg = False

if flg:
    print("Yes")
else:
    print("No")
