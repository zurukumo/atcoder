N = int(input())
w = input().replace(".", "").split()

ret = 0
t = ["TAKAHASHIKUN", "Takahashikun", "takahashikun"]
for w_ in w:
    if w_ in t:
        ret += 1

print(ret)
