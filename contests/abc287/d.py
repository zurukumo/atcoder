S = input()
T = input()

first_match = 0
for i in range(len(T)):
    if S[i] == T[i] or S[i] == "?" or T[i] == "?":
        first_match += 1
    else:
        break
last_match = 0
for i in range(len(T)):
    if S[-(i + 1)] == T[-(i + 1)] or S[-(i + 1)] == "?" or T[-(i + 1)] == "?":
        last_match += 1
    else:
        break

for i in range(len(T) + 1):
    if i <= first_match and len(T) - i <= last_match:
        print("Yes")
    else:
        print("No")
