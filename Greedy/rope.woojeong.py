# input
numRope = int(input())
lst = []
for i in range(numRope):
    lst.append(int(input()))
lst = list(map(int,lst)) # to int
lst.sort() # sorting

# sol
max_w = 0
for k in range(numRope):
    sum_w = lst[k] * (numRope - k)
    if sum_w > max_w:
        max_w = sum_w

print(max_w)
