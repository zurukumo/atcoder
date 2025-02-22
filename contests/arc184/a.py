N, M, Q = map(int, input().split())

perfect_zero = None
has_one = False
global_logs = []
local_logs = []
for i in range(1, 990 + 1):
    if i % 11 == 0:
        if has_one:
            global_logs.append(local_logs)
        else:
            perfect_zero = i

        has_one = False
        local_logs = []
        continue

    print(f"? {i} {i + 1}")
    v = int(input())
    if v == 1:
        has_one = True
    local_logs.append((i, i + 1, v))

ret = [0] * (N + 1)
for local_logs in global_logs:
    print(f"? {local_logs[0][0]} {perfect_zero}")
    v = int(input())
    ret[local_logs[0][0]] = v
    for a, b, x in local_logs:
        v ^= x
        ret[b] = v

for i in range(991, 1001):
    print(f"? {i} {perfect_zero}")
    v = int(input())
    ret[i] = v

print("!", *[i for i in range(N + 1) if ret[i] == 1])
