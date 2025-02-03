N = int(input())
A = [[int(i) for i in input().split()] for _ in range(N)]
B = [[int(i) for i in input().split()] for _ in range(N)]

gax = sum(A[i][0] for i in range(N)) / N
gay = sum(A[i][1] for i in range(N)) / N
gbx = sum(B[i][0] for i in range(N)) / N
gby = sum(B[i][1] for i in range(N)) / N

ma, mb = 0, 0
for (ax, ay), (bx, by) in zip(A, B) :
  ma = max(ma, ((ax - gax) ** 2 + (ay - gay) ** 2))
  mb = max(mb, ((bx - gbx) ** 2 + (by - gby) ** 2))

print((mb / ma) ** 0.5)