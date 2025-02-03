N = input()

for i in range(10):
    M = '0' * i + N
    if M == M[::-1]:
        print('Yes')
        break
else:
    print('No')
