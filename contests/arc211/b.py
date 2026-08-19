X, Y, Z = map(int, input().split())


if X == Y:
    S1 = "0" * Y
    S2 = "0" * Z
    S3 = "0" * Z
else:
    S1 = "0" * Y
    S2 = "0" * X + "1" * Z
    S3 = "1" * Z + "0" * Y

print(len(S1), *[c for c in S1])
print(len(S2), *[c for c in S2])
print(len(S3), *[c for c in S3])
