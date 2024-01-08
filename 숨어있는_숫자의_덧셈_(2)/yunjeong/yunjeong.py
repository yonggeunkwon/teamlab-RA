def solution(my_string):
    for i in my_string:
        if i.isdigit() == False :
            my_string = my_string.replace(i , " ")  # 글자를 공백으로
    # print(my_string)

    # 공백기준 split() _ 구분자 없음 : split()의 결과값은 str형의 데이터들을 list로 저장
    new_list = my_string.split()
    # print(new_list)

    integers =[]
    for k in new_list :
        integers.append(int(k))    # new_list의 숫자들을 int형으로 바꾸기
    # print(integers)

    answer= sum(integers)          # sum() : 리스트의 요소들 모두를 더한 값
    # print(answer)
    return answer

ex = "1dfte98f12"
result = solution(ex)
print(result)