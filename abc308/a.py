S = [int(i) for i in input().split()]


for i in range(len(S)):
    if i + 1 < len(S) and not (S[i] <= S[i + 1]):
        print("No")
        break
    if not (100 <= S[i] <= 675 and S[i] % 25 == 0):
        print("No")
        break
else:
    print("Yes")
