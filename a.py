# N = int(input())
# print(''.join(map(str, range(2*N))))
# S = input()

from random import shuffle, randint

counter = 0
while counter < 1 :
    N = 5
    # print(''.join(map(str, range(2*N))))
    # S = []
    # S.append('B')
    # for _ in range(2 * N - 2) :
        # S.append('BW'[randint(0, 1)])
    # S.append('B')
    # print(''.join(S))
    S = 'BBWWBBWWBB'
    print(S)
    T = [0 if s == 'W' else 1 for s in S]

    def rec(T, level, visited, q) :
        if sum(T) == 0 and visited == [True] * (2 * N) :
            print(sorted(q))
        print('***' * level, T, visited)
            
        for i in range(2 * N) :
            if not visited[i] :
                visited[i] = True
                
                for j in range(i + 1, 2 * N) :
                    if not visited[j] :
                        visited[j] = True
                        U = T[::]
                        for k in range(i, j + 1) :
                            U[k] ^= 1
                        q.append((i, j))
                        rec(U, level + 1, visited, q)
                        visited[j] = False
                        q.pop()
                        
                visited[i] = False
                
                break
                
    rec(T, 0, [False] * (2 * N), [])
    counter += 1