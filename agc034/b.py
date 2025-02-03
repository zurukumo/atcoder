s = list(input())

ret = 0
i = 0
a = 0
bc = 0

while True:
    while i < len(s) and s[i] == "A":
        a += 1
        i += 1

    while i < len(s) - 1 and s[i : i + 2] == ["B", "C"]:
        bc += 1
        i += 2

    ret += a * bc

    bc = 0

    if i < len(s) and s[i] != "A":
        a = 0

    while i < len(s) and s[i] != "A":
        i += 1

    if i >= len(s) - 1:
        break


print(ret)
