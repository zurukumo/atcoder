N = int(input())
c = input()

count = [c.count(str(i)) for i in range(1, 5)]
print(max(count), min(count))