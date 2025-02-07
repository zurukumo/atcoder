L = int(input())
B = [int(input()) for _ in range(L)]

s = 0
for i in range(L):
    s ^= B[i]

if s == 0:
    a = 0
    for i in range(L):
        print(a)
        a = B[i] ^ a

else:
    print(-1)
