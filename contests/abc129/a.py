P, Q, R = map(int, input().split())

# print(min(P + Q, Q + R, R + P))
print(P + Q + R - max(P, Q, R))
