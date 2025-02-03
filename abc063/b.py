import sys

input = sys.stdin.readline

S = input()
T = sorted(S)
for i in range(1, len(T)):
    if T[i] == T[i - 1]:
        print("no")
        break
else:
    print("yes")
