num = int(input())
ropes = []
ropes.append(int(input()))
for i in range(1, num) :
    ropes.append(int(input()))
ropes = sorted(ropes)
maxi = 0
for i in range(num):
    maxi = max(maxi, ropes[i] * (num - i))
print(maxi)