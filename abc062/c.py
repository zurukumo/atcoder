H, W = map(int, input().split())

def diff(a, b, c) :
    return max([a, b, c]) - min([a, b, c])

def div2(H, W, s) :
    h2, w2 = H//2, W//2
    m = float('inf')
    m = min(m, diff(s, h2*W, (H-h2)*W))
    m = min(m, diff(s, w2*H, (W-w2)*H))
    return m
    

def div3(H, W) :
    m = float('inf')
    h3, w3 = H//3, W//3
    m = min(m, div2(H-h3, W, h3*W))
    m = min(m, div2(H-(h3+1), W, (h3+1)*W))
    m = min(m, div2(H, W-w3, w3*H))
    m = min(m, div2(H, W-(w3+1), (w3+1)*H))
    return m
    
print(div3(H, W))