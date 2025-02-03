N = int(input())
t = [int(i) for i in input().split()]
v = [int(i) for i in input().split()]

for i in range(1, N) :
        t[i] += t[i-1]
        
l = [t_ + v_ for t_, v_ in zip(t, v[1:]+[0])]
for i in range(N-2, -1, -1) :
    l[i] = min(l[i], l[i+1])
    
cur_v, cur_t = 0, 0
ret = 0
for i in range(N) :
    t1 = v[i] - cur_v + cur_t
    t2 = l[i] - v[i]
    if t[i] < t1 <= t2 :
        ret += (2 * cur_v + t[i] - cur_t) * (t[i] - cur_t) / 2
        cur_v = cur_v + t[i] - cur_t
        
    elif cur_t <= t1 <= t2 :
        ret += (t1 - cur_t) * (cur_v + v[i]) / 2
        if t2 <= t[i] :
            ret += (t2 - t1) * v[i]
            ret += (t[i] - t2) * (v[i] + l[i] - t[i]) / 2
            cur_v = l[i] - t[i]
        else :
            ret += (t[i] - t1) * v[i]
            cur_v = v[i]
    
    else :
        t3 = (l[i] + cur_t - cur_v) / 2
        if t3 >= t[i] :
            t3 = t[i]
        ret += (t3 - cur_t) * (2 * cur_v + t3 - cur_t) / 2
        ret += (t[i] - t3) * (2 * (cur_v + t3 - cur_t) - (t[i] - t3)) / 2
        if t3 == t[i] :
            cur_v = cur_v + t[i] - cur_t
        else :
            cur_v = l[i] - t[i]
    cur_t = t[i]
    
print(ret)