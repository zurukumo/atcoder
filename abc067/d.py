import sys
input = sys.stdin.readline

N = int(input())

v = [[] for _ in range(N)]
for _ in range(N-1) :
    a, b = map(int, input().split())
    v[a-1].append(b-1)
    v[b-1].append(a-1)

qa, qb = [0], [N-1]
sa, sb = 0, 0
visited = [False] * N
visited[0] = visited[N-1] = True

while qa or qb :
    qa_ = []
    while qa :
        cur = qa.pop()
        for nex in v[cur] :
            if not visited[nex] :
                visited[nex] = True
                qa_.append(nex)
                sa += 1
    qa = qa_
    
    qb_ = []
    while qb :
        cur = qb.pop()
        for nex in v[cur] :
            if not visited[nex] :
                visited[nex] = True
                qb_.append(nex)
                sb += 1
    qb = qb_
    
if sa > sb :
    print('Fennec')
else :
    print('Snuke')