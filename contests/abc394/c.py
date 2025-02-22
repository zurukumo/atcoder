S = input()

S = list(S)

for i in range(len(S) - 1):
    j = i
    while j >= 0 and S[j] == "W" and S[j + 1] == "A":
        S[j], S[j + 1] = "A", "C"
        j -= 1

print("".join(S))
