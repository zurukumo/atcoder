X, Y, A, B, C = map(int, input().split())
p = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]
r = [int(i) for i in input().split()]

p.sort()
q.sort()
r.sort(reverse=True)

p = p[-X:]
q = q[-Y:]

pi = 0
qi = 0

for rv in r:
    if 0 <= pi < X and 0 <= qi < Y:
        if p[pi] <= q[qi] and p[pi] < rv:
            p[pi] = rv
            pi += 1
            continue
        if q[qi] <= p[pi] and q[qi] < rv:
            q[qi] = rv
            qi += 1
            continue

    if 0 <= pi < X and p[pi] < rv:
        p[pi] = rv
        pi += 1
        continue

    if 0 <= qi < Y and q[qi] < rv:
        q[qi] = rv
        qi += 1
        continue

print(sum(p[:X]) + sum(q[:Y]))
