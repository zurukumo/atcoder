S = input()

for i in range(26):
    if chr(ord("a") + i) not in S:
        print(chr(ord("a") + i))
        exit()
