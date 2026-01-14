import sys
input = sys.stdin.readline
M = int(input())
N = int(input())


prime = []
res1 = 0
res2 = 0

for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        prime.append(i)

if prime:
    res1 = sum(prime)
    res2 = prime[0]
    print(res1)
    print(res2)
else:
    print(-1)