A, B, K, L = map(int, input().split())

ret = 0
if B / L < A :
    ret += K // L * B
    K %= L
    ret = min(ret + K * A, ret + B)
else :
    ret = K * A

print(ret)