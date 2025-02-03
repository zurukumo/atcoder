s = input()
x, y = map(int, input().split())

count = [[], []]
now = 0
for f in s.split('T') :
    count[now].append(len(f))
    now ^= 1

def solve() :
    dp = set([count[0][0]])
    for c in count[0][1:] :
        if c == 0 :
            continue
        dp_ = set()
        for xi in dp :
            dp_.add(xi+c)
            dp_.add(xi-c)
        dp = dp_
    if not x in dp :
        return 'No'
    
    dp = set([0])
    for c in count[1] :
        if c == 0 :
            continue
        dp_ = set()
        for yi in dp :
            dp_.add(yi+c)
            dp_.add(yi-c)
        dp = dp_
    if not y in dp :
        return 'No'
    return 'Yes'

print(solve())