T = int(input())
for _ in range(T):
    L, R = map(int, input().split())
    if len(str(R)) == len(str(L)):
        print(R - L + 1)
    else:
        r1 = int(str(R)[:-1])
        if str(R)[0] == "1":
            r2 = int(str(R)[1:])
        else:
            r2 = int("9" * (len(str(R)) - 1))

        ret = R - max(r1, r2, L - 1)
        print(ret)


# def fast(L, R):
#     if len(str(R)) == len(str(L)):
#         return R - L + 1
#     else:
#         r1 = int(str(R)[:-1])
#         if str(R)[0] == "1":
#             r2 = int(str(R)[1:])
#         else:
#             r2 = int("9" * (len(str(R)) - 1))

#         print("r1 to r2 dayo", r1, r2)

#         ret = R - max(r1, r2, L - 1)
#         return ret


# def slow(L, R):
#     done = []
#     while R >= L:
#         for d in done:
#             if str(R) in str(d):
#                 break
#         else:
#             done.append(R)
#         R -= 1
#     return len(done)


# import random

# while True:
#     L, R = random.randint(1, 1000), random.randint(1, 1000)
#     L, R = min(L, R), max(L, R)
#     if fast(L, R) == slow(L, R):
#         print("OK")
#     else:
#         print(L, R)
#         print(fast(L, R), slow(L, R))
#         break
