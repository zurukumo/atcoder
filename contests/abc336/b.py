N = int(input())

ret = 0
bit = list(bin(N))
while bit[-1] == "0":
    bit.pop()
    ret += 1
print(ret)
