N, K = map(int, input().split())
S = input()

T = ""
for c in S:
    if c == "o" and K > 0:
        T += "o"
        K -= 1
    else:
        T += "x"
print(T)
