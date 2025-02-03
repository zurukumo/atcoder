N, K = map(int, input().split())

done = set([])
for _ in range(K) :
  d = int(input())
  A = [int(i) for i in input().split()]
  done |= set(A)
  
print(N - len(done))