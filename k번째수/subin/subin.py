def solution(array, commands):
    result_list = []
    for list in commands:                #먼저 for문을 이용해서 commands 안에 있는 리스트부터 쪼개버리기
        i = list[0]                      #i, j , k 설정
        j = list[1]
        k = list[2]
        
        slicing = array[i -1 : j]        #i번쨰부터 j번째까지 슬라이싱을 하자..
        sorted_slicing = sorted(slicing) #그런데 정렬해야하네 ㅋㅋ
        result = sorted_slicing[k-1]     #슬라이싱을 한 것에 k번째 숫자를 뽑아내자..
        
        result_list.append(result)       #빈 리스트에 추가해주기
    return result_list

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))