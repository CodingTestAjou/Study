num_of_person = int(input())
p_lst = input().split()
p_lst = list(map(int, p_lst)) # to int
p_lst.sort() # sorting

sum_p = 0

for i in range(num_of_person):
    temp = p_lst[i] * (num_of_person - i)
    sum_p = sum_p + temp

print(sum_p)
