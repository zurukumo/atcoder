ABC = [int(i) for i in input().split()]
ABC.sort()

diff = ABC[2] - ABC[1]
ret = diff
ABC[0] += diff
ABC[1] += diff

ret += (ABC[1] - ABC[0]) // 2
if (ABC[1] - ABC[0]) % 2 == 1 :
    ret += 2
    
print(ret)