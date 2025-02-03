N = int(input())
a, b = map(int, input().split())
K = int(input())
P = [int(i) for i in input().split()]

if len(set([a, b] + P)) == len([a, b] + P) :
    print('YES')
else :
    print('NO')
    