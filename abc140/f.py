N = int(input())
S = [int(i) for i in input().split()]


def solve():
    S.sort()
    par = [S.pop()]
    rst = S
    for _ in range(N):
        n_par = []
        n_rst = []

        for p in par[::-1]:
            flg = True
            while rst:
                if rst[-1] < p:
                    n_par.append(rst.pop())
                    flg = False
                    break
                else:
                    n_rst.append(rst.pop())
            if flg:
                return "No"

        par += n_par
        par.sort()
        rst += n_rst
        rst.sort()

    return "Yes"


print(solve())
