import collections

S = input()

ret = 0
mem = collections.defaultdict(int)
mem[S[-1]] += 1
mem[S[-2]] += 1
for i in range(len(S) - 3, -1, -1):
    mem[S[i]] += 1
    if S[i] == S[i + 1] and S[i] != S[i + 2]:
        ret += len(S) - i - mem[S[i]]
        mem = collections.defaultdict(int)
        mem[S[i]] = len(S) - i

print(ret)
