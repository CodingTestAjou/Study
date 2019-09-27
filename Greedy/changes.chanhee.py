coin = [500, 100, 50, 10, 5, 1]
money = 1000 - int(input())
count = 0
idx = 0
while (money > 0):
    if (money >= coin[idx]):
        money -= coin[idx]
        count += 1
    else:
        idx += 1
print(count)