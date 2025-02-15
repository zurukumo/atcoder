N = int(input())
S = input()

ls = 0
lc = 0
rs = 0
rc = 0
for i, c in enumerate(S):
    if c == "1":
        rs += i + 1
        rc += 1

ret = float("inf")
for c in S:
    rs -= rc
    ls += lc
    if c == "1":
        rc -= 1
    left = ls - lc * (lc - 1) // 2 - lc
    right = rs - rc * (rc - 1) // 2 - rc
    tmp = left + right
    if c == "0":
        tmp += min(lc, rc)
    ret = min(ret, tmp)
    if c == "1":
        lc += 1
print(ret)
