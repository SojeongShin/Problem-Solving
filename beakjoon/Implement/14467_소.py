# 소가 길을 건너간 이유 1
num = 0
observed = int(input())
cows = [None] * 11
for _ in range(observed):
    cow, position = map(int, input().split())
    if cows[cow] is not None and cows[cow] != position:
        num += 1
    cows[cow] = position

print(num)

    