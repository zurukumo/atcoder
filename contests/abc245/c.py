N, K = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

pre = set([A[0], B[0]])
for a, b in zip(A[1:], B[1:]):
    cur = set(())
    for x in pre:
        if abs(x - a) <= K:
            cur.add(a)
        if abs(x - b) <= K:
            cur.add(b)
    pre = cur

if pre:
    print("Yes")
else:
    print("No")
