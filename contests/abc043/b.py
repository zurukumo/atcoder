s = input()

ret = []
for s_ in s:
    if s_ == "B":
        if len(ret) != 0:
            ret.pop()
    else:
        ret.append(s_)

print("".join(ret))
