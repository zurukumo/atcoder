N = int(input())
md = [[int(i) for i in input().split("/")] for _ in range(N)]

holiday = [[False] * 32 for _ in range(13)]
for m, d in md:
    holiday[m][d] = True

calendar = []
week = 0
flag = 0
for i in range(1, 13):
    if i == 2:
        D = 29
    elif i in [4, 6, 9, 11]:
        D = 30
    else:
        D = 31

    for j in range(1, D + 1):
        if week == 0 or week == 6:
            calendar.append(1)
            if holiday[i][j]:
                flag += 1
        else:
            if holiday[i][j]:
                calendar.append(1)
            elif flag > 0:
                calendar.append(1)
                flag -= 1
            else:
                calendar.append(0)

        week += 1
        week %= 7

for i in range(1, 366):
    if calendar[i] != 0:
        calendar[i] += calendar[i - 1]
print(max(calendar))
