S = input()

ret = [0] * 26
for s in S:
    ret[ord(s) - 97] = 1

for i in range(26):
    if ret[i] == 0:
        print(chr(i + 97))
        break
else:
    print("None")
