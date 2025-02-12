H, W = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(H)]

for i in range(H):
    row = ""
    for v in A[i]:
        if v == 0:
            row += "."
        else:
            row += chr(ord("A") + v - 1)
    print(row)
