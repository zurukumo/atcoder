N, K = map(int, input().split())
S = input()

T = list(S) + ["."]
N += 1

for i in range(N):
    if T[i] == "o":
        K -= 1
        if 0 <= i - 1:
            T[i - 1] = "."
        if i + 1 < N:
            T[i + 1] = "."

max_o = 0
cnt = 0
for i in range(N):
    if T[i] == "?":
        cnt += 1
    else:
        max_o += (cnt + 1) // 2
        cnt = 0

if max_o == K:
    cnt = 0
    for i in range(N):
        if T[i] != "?":
            if cnt % 2 == 1:
                j = i - 1
                is_o = True
                while j >= 0 and T[j] == "?":
                    if is_o:
                        T[j] = "o"
                    else:
                        T[j] = "."
                    is_o = not is_o
                    j -= 1
            cnt = 0
        else:
            cnt += 1
elif K == 0:
    for i in range(N):
        if T[i] == "?":
            T[i] = "."

T.pop()
print("".join(T))
