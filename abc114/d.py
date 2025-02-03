N = int(input())

prime = [0] * (N + 1)
for i in range(1, N + 1) :
    while i % 2 == 0 :
        i //= 2
        prime[2] += 1
    j = 3
    while i != 1 :
        while i % j == 0 :
            i //= j
            prime[j] += 1
        j += 2

# 3 5 15 25 75
over = [0] * 5

for i in range(1, N + 1) :
    if 74 <= prime[i] :
        over[4] += 1
    elif 24 <= prime[i] :
        over[3] += 1
    elif 14 <= prime[i] :
        over[2] += 1
    elif 4 <= prime[i] :
        over[1] += 1
    elif 2 <= prime[i] :
        over[0] += 1
        
s = [sum(over[i:]) for i in range(5)]

ret = 0
# 3*5*5
ret += over[0] * s[1] * (s[1] - 1) // 2
ret += s[1] * (s[1] - 1) * (s[1] - 2) // 2
# 3*25
ret += (over[0] + over[1] + over[2]) * s[3]
ret += s[3] * (s[3] - 1)
# 5*15
ret += over[1] * s[2]
ret += s[2] * (s[2] - 1)
# 75
ret += over[4]
print(ret)