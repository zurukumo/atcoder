N = int(input())
S = input()
T = input()

ret = 0
ss = []
ts = []
for i, (s, t) in enumerate(zip(S, T)):
    if t == "1":
        ts.append(i)

    if s == "1":
        if ss:
            ret += i - ss.pop() - 1 + 1
        elif ts:
            ret += i - ts.pop()
        else:
            ss.append(i)

if not ss and not ts:
    print(ret)
else:
    print(-1)
