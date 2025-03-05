import collections

N = int(input())
S = input().split()

revS = [list(s[::-1]) for s in S]

ret = 0
queue = collections.deque([revS])
while queue:
    new_slist = collections.defaultdict(lambda: [])
    slist = queue.popleft()
    for s in slist:
        if s:
            last = s.pop()
            new_slist[last].append(s)
    for v in new_slist.values():
        ret += len(v) * (len(v) - 1) // 2
    queue.extend(v for v in new_slist.values() if len(v) > 1)

print(ret)
