AB, BC, CA = map(int, input().split())

print(min(AB*BC, BC*CA, CA*AB) // 2)