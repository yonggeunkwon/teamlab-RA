# 전국 대회 선발 고사

rank = [3,7,2,5,4,6,1]
attendance = [False, True, True, True, True, False, False]

item_list = []
result_list = []
for r in zip(rank,attendance):
    item_list.append(list(r))

for i in item_list:
    if i[1] == True:
        result_list.append(i)

result_list.sort()

a = item_list.index(result_list[0])
b = item_list.index(result_list[1])
c = item_list.index(result_list[2])

print(10000*a+100*b+c)