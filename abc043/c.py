N = int(input())
a = [int(i) for i in input().split()]

ret = float('inf')
for i in range(-100, 101) :
    ret = min(ret, sum([(a_ - i) ** 2 for a_ in a]))
    
print(ret)