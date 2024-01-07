def solution(my_string):
    my_list = []                # 코드6에서 빈 리스트의 필요성을 느껴, 위로 올라와 새로운 리스트 상정
    for i in my_string:   
        # print(i)              # 확인용
        if i.isdigit()==True:   # 나 i.isdigit() 안 쓰고 my_string.isdigit() 썼었음.for문을 쓴 이유 계속 상기하기. 문자열 하나하나 떼어보기 위해서 for문 쓴겨. 문자열 전체가 0을 포함한 양의 정수로 이루어져야 True를 반환하는 함수이므로, for문에 범위로 my_string값을 받아서 문자열 한 자 한 자 isdigit()함수를 거친다
            my_list.append(int(i)) # 위의 if문에서 True 판정된 숫자들을 담을 리스트가 필요함. 오름차순 정렬 전에 여기에 리스트가 있으면 될 듯.
            # print(my_list)      # 이게 cmd창의 [숫자] 보이게 하는
        else:                   # 생략가능
            None
    answer = sorted(my_list)     #list.sort()는 기존의 리스트를 정렬함 & sorted(list)는 정렬된 리스트를 새로이 만듦
    # print(answer)              # digh
    return answer



ex = 'ag9G254'
result = solution(ex)
print(result)