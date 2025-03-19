A, B = map(int, input().split())

plus = [i for i in range(1, A + 1)]
minus = [-i for i in range(1, B + 1)]

sp = sum(plus)
sm = sum(minus)

if sp > -sm:
    diff = sp - (-sm)
    minus[-1] -= diff
elif sp < -sm:
    diff = -sm - sp
    plus[-1] += diff

print(*(plus + minus))
