N, H = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(N)]
amax = max(ab)[0]

def solve(H) :
    ret = 0
    ab.sort(key=lambda x: x[1], reverse=True)
    for a, b in ab :
        if b > amax :
            H -= b
            ret += 1
        else :
            break
            
        if H <= 0 :
            return ret
            
    ret += (H + amax - 1) // amax
    return ret

print(solve(H))