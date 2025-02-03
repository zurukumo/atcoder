from sortedcontainers import SortedList

N, K, Q = map(int, input().split())
XY = [[int(i) for i in input().split()] for _ in range(Q)]

s = 0
current_v = [0] * N
lset = SortedList()
rset = SortedList()


for x, y in XY:
    x -= 1

    # 古い値があったら削除
    if current_v[x] in lset:
        lset.remove(current_v[x])
        s -= current_v[x]
    elif current_v[x] in rset:
        rset.remove(current_v[x])

    # 新しい値を追加
    s += y
    lset.add(y)
    current_v[x] = y

    # バランス処理
    while len(lset) > K:
        v = lset.pop(0)
        rset.add(v)
        s -= v
    while len(lset) < K and len(rset) > 0:
        v = rset.pop(-1)
        lset.add(v)
        s += v
    while len(lset) > 0 and len(rset) > 0 and lset[0] < rset[-1]:
        lv = lset.pop(0)
        rv = rset.pop(-1)
        lset.add(rv)
        rset.add(lv)
        s += rv - lv

    print(s)
