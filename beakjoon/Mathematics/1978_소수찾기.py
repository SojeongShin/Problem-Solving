import sys

input = sys.stdin.readline

primes = 0
n = int(input())
nums = list(map(int, input().split()))

for i in nums:
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        primes += 1

print(primes)