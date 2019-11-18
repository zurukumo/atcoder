# T = int(input())
# ABCD = [[int(i) for i in input().split()] for _ in range()]

from random import randint
n = 0
while n < 50 :
    A, B, C, D = (randint(1, 20) for _ in range(4))
    # A, B, C, D = 9, 7, 6, 9

    # print(A, B, C, D)
    origin = [A, B, C, D]
    
    count = 0
    while A >= B and count < 1000 :
        A -= B
        # print('Morning', A)
        if A <= C :
            A += D
            # print('Evening', A)
        count += 1
        
    if count == 1000 :
        print(origin)
        n += 1
    # break