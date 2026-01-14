money = int(input())
count = -1

for k in range(money // 5, -1, -1):
    rem = money - k * 5
    if rem % 2 == 0:
        count = k + rem // 2
        break
print(count)

