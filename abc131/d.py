N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N)]

AB.sort(key=lambda x: x[1])

t = 0
for A, B in AB:
    t += A
    if t > B:
        print("No")
        break
else:
    print("Yes")
