S1 = input()
S2 = input()
S3 = input()
S4 = input()

Slist = [S1, S2, S3, S4]
if len(set(Slist)) == 4:
    print('Yes')
else:
    print('No')
