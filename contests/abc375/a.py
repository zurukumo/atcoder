N = int(input())
S = input()

ret = 0
for i in range(N - 2):
    if S[i : i + 3] == "#.#":
        ret += 1
print(ret)
