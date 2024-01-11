quiz = ["3 - 4 = -3", "5 + 6 = 11"]
new_list = []
result_list = []

for i in quiz:
    new = i.split('=')
    new_list.append(new)
print(new_list)

for f in range(len(new_list)):
    if eval(new_list[f][0]) == int(new_list[f][1]):
        result_list.append('O')
    else:
        result_list.append('X')
        
print(result_list)


# for calculate_num in new_list:
#     calculate = calculate_num[0].replace(" ","")
#     print(calculate)