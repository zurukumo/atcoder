W, H = map(int, input().split())

mod = 998244353

fib = [1, 1]
for _ in range(2 ** 6 + 10):
    fib.append((fib[-1] + fib[-2]) % mod)

mat = [[0] * (2 ** W) for _ in range(2 ** W)]
mem = []
for i in range(2 ** W):
    xi = [(i // (2 ** k)) % 2 for k in range(W)]
    for j in range(2 ** W):
        xj = [(j // (2 ** k)) % 2 for k in range(W)]
        for k in range(W):
            if xi[k] == 1 and xj[k] == 1:
                break
        else:
            xj.append(1)
            s = 1
            c = 0
            for k in range(W + 1):
                if xj[k] != 0 or xi[k] == 1:
                    s *= fib[c]
                    c = 0
                else:
                    c += 1

            mat[i][j] = s % mod


def dot(A, B):
    x = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            x[i][j] = sum([A[i][k] * B[k][j] for k in range(len(B))]) % mod
    return x


for _ in range(50):
    mem.append(mat)
    mat = dot(mat, mat)


cmat = None
for i in range(49, -1, -1):
    if H >= 2 ** i:
        if cmat is None:
            cmat = mem[i]
        else:
            cmat = dot(cmat, mem[i])

        H -= 2 ** i

ret = 0
init = [[0] * (2 ** W)]
init[0][0] = 1
cmat = dot(init, cmat)
for i in range(2 ** W):
    xi = [(i // (2 ** k)) % 2 for k in range(W)]
    if 1 not in xi:
        ret += cmat[0][i]
        ret %= mod

print(ret % mod)
