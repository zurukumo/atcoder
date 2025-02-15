S = input()

if sum(1 for c in S if c.isupper()) > sum(1 for c in S if c.islower()):
    print(S.upper())
else:
    print(S.lower())
