from collections import defaultdict

N = int(input())
s1 = input()
s2 = input()

v = defaultdict(lambda: [])
for i in range(N):
    v[s1[i]].append(s2[i])
    v[s2[i]].append(s1[i])

ret = 1
visited = defaultdict(lambda: False)
for i in range(N):
    if visited[s1[i]]:
        continue

    visited[s1[i]] = True
    q = [s1[i]]
    flag = False
    while q:
        cur = q.pop()
        if cur in "0123456789":
            flag = True

        for nex in v[cur]:
            if not visited[nex]:
                visited[nex] = True
                q.append(nex)

    if not flag:
        if i == 0:
            ret *= 9
        else:
            ret *= 10

print(ret)
