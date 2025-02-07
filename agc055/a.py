N = int(input())
S = [ord(c) - ord("A") for c in input()]

T = [-1] * (3 * N)

s = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i, c in enumerate(S):
    s[i // N][c] += 1

for i in range(1, 10):
    max_k = (-1, -1, -1)
    max_v = -float("inf")
    for x, y, z in [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]:
        v = min(s[0][x], s[1][y], s[2][z])
        if v > max_v:
            max_k = (x, y, z)
            max_v = v

    x, y, z = max_k
    vs = [max_v] * 3
    s[0][x] -= max_v
    s[1][y] -= max_v
    s[2][z] -= max_v

    for j in range(3 * N):
        if j // N == 0 and T[j] == -1 and vs[x] > 0 and S[j] == x:
            T[j] = i
            vs[x] -= 1
        elif j // N == 1 and T[j] == -1 and vs[y] > 0 and S[j] == y:
            T[j] = i
            vs[y] -= 1
        elif j // N == 2 and T[j] == -1 and vs[z] > 0 and S[j] == z:
            T[j] = i
            vs[z] -= 1


print("".join(map(str, T)))
