from collections import defaultdict

N = int(input())
a = [int(i) for i in input().split()]

counter = defaultdict(int)
for i in range(N) :
    counter[a[i]-1] += 1
    counter[a[i]] += 1
    counter[a[i]+1] += 1

print(max(counter.values()))