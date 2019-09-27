numOfPeople = int(input())
times = sorted(list(map(int, (input()).split())))
total = 0
wait = 0
for i in range(numOfPeople):
    wait = wait + times[i]
    total = total + wait
print(total)