s = input()
k = int(input())

ret = set()
for i in range(len(s) - k + 1):
    ret.add(s[i : i + k])
print(len(ret))
