s = input()

i = s.find("A")
j = s[::-1].find("Z")

print(len(s) - j - i)
