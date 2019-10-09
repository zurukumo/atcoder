N, M = map(int, input().split())
AB = [[] for _ in range(N)]
for _ in range(M) :
    A, B = map(int, input().split())
    AB[A-1].append(B-1)
    
# 方針
# グラフは連結成分ごとに考える
# ある頂点を削除したときでも閉路が存在すればどんどん消していく