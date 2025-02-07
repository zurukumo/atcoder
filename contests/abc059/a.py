s1, s2, s3 = input().split()

print(("").join([chr(ord(s) - 32) for s in [s1[0], s2[0], s3[0]]]))
