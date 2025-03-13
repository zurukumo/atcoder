T = int(input())
for _ in range(T):
    K = int(input())
    ret = ""
    pre = None
    for i in range(15, -1, -1):
        for j in range(9, -1, -1):
            if j == pre:
                continue

            if pre is None:
                if j > 0:
                    rest = (j - 1) * (9**i) + (9 * 9**i - 9) // 8
                else:
                    continue
            elif j > pre:
                rest = (j - 1) * (9**i)
            else:
                rest = j * (9**i)
            if K > rest:
                K -= rest
                ret += str(j)
                pre = j
                break
    print(ret)
