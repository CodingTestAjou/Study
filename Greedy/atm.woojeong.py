getMoney = int(input())
myMoney = 1000
rest = myMoney - getMoney

coin_lst = [500, 100, 50, 10, 5, 1]
cnt = 0

for c in coin_lst:
    k = int(rest / c)
    if k > 0 :
        cnt = cnt + k
        rest = rest % c

print(cnt)
