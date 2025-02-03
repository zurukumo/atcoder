N = int(input())

if N == 0 :
    print(0)
else :
    ret = ''
    while N != 1 :
        ret += str(N % 2)
        N = -(N // 2)
        
    print('1' + ret[::-1])