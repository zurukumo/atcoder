N = int(input())
W = input().split()

ng_words = ["and", "not", "that", "the", "you"]
for word in ng_words:
    if word in W:
        print("Yes")
        break
else:
    print("No")
