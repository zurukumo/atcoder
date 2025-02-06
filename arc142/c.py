N = int(input())

one = [-1] * (N + 1)
two = [-1] * (N + 1)
for i in range(3, N + 1):
    print(f"? 1 {i}")
    d = int(input())
    one[i] = d
    print(f"? 2 {i}")
    d = int(input())
    two[i] = d

# 通常の場合
ret = float("inf")
sum3 = []
for i in range(3, N + 1):
    ret = min(ret, one[i] + two[i])
    if one[i] + two[i] == 3:
        sum3.append(i)

# sum3の長さが0でも2でもなければ1と2は隣り合っている
if len(sum3) != 0 and len(sum3) != 2:
    ret = 1

# sum3の長さが2でも、その2つが隣り合っていなければ1と2は隣り合っている
if len(sum3) == 2:
    print(f"? {sum3[0]} {sum3[1]}")
    d = int(input())
    if d != 1:
        ret = 1

print(f"! {ret}")
