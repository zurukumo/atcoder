N = int(input())

for i in range(1, 10):
    if N % i == 0 and N // i < 10:
        print("Yes")
        break
else:
    print("No")
