s = input()
n = len(s)

count = 1
c = s[0]
i = 1
t = ""

while i < n:
    if s[i] == c:
        count += 1
    else:
        t += c + str(count)
        count = 1
        c = s[i]

    i += 1

t += c + str(count)

print(t)
