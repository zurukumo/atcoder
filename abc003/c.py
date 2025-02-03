N, K = map(int, input().split())
R = list(map(int, input().split()))

R.sort()
rate = 0

for i in range(K) :
	rate += R[N-K+i] * (2 ** i)

print(rate / (2 ** K))