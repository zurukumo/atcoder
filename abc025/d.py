from collections import defaultdict

x = [int(i)-1 for _ in range(5) for i in input().split()]
MOD = 10 ** 9 + 7

pos = [-1] * 25
emp = []
for i in range(25) :
    if x[i] >= 0 :
        pos[x[i]] = i
    else :
        emp.append(i)

# iのj文字目に追加できるか確認する
def judge(i, j) :
    # iのj文字目が1なら駄目
    if (i >> j) & 1 == 1 :
        return False
    
    x, y = j % 5, j // 5
    
    # 横のチェック iのj-1文字目とj+1文字目が違ったら駄目
    if 1 <= x <= 3 :
        if ((i >> (j-1)) & 1) ^ ((i >> (j+1)) & 1) :
            return False
    # 縦のチェック iのj-5文字目とj+5文字目が違ったら駄目
    if 1 <= y <= 3 :
        if ((i >> (j-5)) & 1) ^ ((i >> (j+5)) & 1) :
            return False
            
    return True
    
dp = defaultdict(int)
dp[0] = 1

cur = set([0])
# i -> 追加する数
for i in range(25) :
    next = set()
    dp_ = defaultdict(int)
    
    # iの場所が入力で指定されている場合
    if pos[i] >= 0 :
        for c in cur :
            if judge(c, pos[i]) :
                next.add(c^(1<<pos[i]))
    
    # iの場所が入力で指定されていない場合empに入れる
    else :
        for c in cur :
            for j in emp :
                if judge(c, j) :
                    next.add(c^(1<<j))
    
    # dpの更新
    for n in next :
        ret = 0
        for j in range(25) :
            if (n >> j) & 1 == 1 and judge(n^(1<<j), j) :
                ret += dp[n^(1<<j)]
                ret %= MOD
        
        dp_[n] = ret
                    
    cur = next
    dp = dp_
    
print(dp[(1<<25)-1])