from collections import Counter

N = int(input())
a = [int(i) for i in input().split()]

schedule = []
m = 0
if -min(a) > max(a) :
    mv = min(a)
    mi = a.index(mv)
    
    for i in range(N-2, -1, -1) :
        while a[i] > a[i + 1] :
            a[i] += mv
            schedule.append([mi+1, i+1])
            if a[i] < mv :
                mv = a[i]
                mi = i
            m += 1
else :
    Mv = max(a)
    Mi = a.index(Mv)
    
    for i in range(1, N) :
        while a[i-1] > a[i] :
            a[i] += Mv
            schedule.append([Mi+1, i+1])
            if a[i] > Mv :
                Mv = a[i]
                Mi = i
            m += 1

print(m)
for sch in schedule :
    print(*sch)