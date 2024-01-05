# A. 알파벳(문자)을 언더바로 바꿔주기
# plus_list = []
# for i  in my_string:
#     if i.isdigit() == True :
#         plus_list.append(i)
#     else:
#         plus_list.append("_")

# print(plus_list)

## A와 a의 차이 -> a는 리스트에 담겨져서 나오고 , b는 문자열 자체에서 문자만 공백

def solution(my_string):
    # a. i가 숫자가 아니면 공백으로 바꿔라
    for i in my_string:
        if i.isdigit() == False :
            my_string = my_string.replace(i , " ")

    # b. " " 기준으로 split()하여 -> list받기
    split_my_list = my_string.split()
    #print(split_my_list)
    
    # c. split된 값들을 str형이니 int값을 바꿔주기
    num =[]
    for j in split_my_list :
        num.append(int(j))
    #print(num)
    
    # d. 값을 다 더해주기
    num_sum = sum(num)
    #print(num_sum)
    return num_sum

my_string = "aB1jki2Afo34sd"
result = solution(my_string)
print(result)