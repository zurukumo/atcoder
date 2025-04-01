S = input()

for i, c in enumerate(S):
    if S.count(c) == 1:
        print(i + 1)
        break
