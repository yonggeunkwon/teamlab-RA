def solution(my_string):
    #숫자들만 넣어줄 리스트 생성
    num = [] 
    
    #하나씩 다 쪼개
    for i in my_string :
        #print(i)

    #i가 숫자가 맞다면 num에 추가 (정수로)
        if i.isdigit() == True :
            num.append(int(i))
            #print(num) 
    
    #num에 들어가 있는 숫자들을 오름차순으로 정렬
    answer = sorted(num)  
    return answer

string = "hi12392" 

#solution() -> 괄호 속 매개변수my_string에 string을 넣고 돌린 결과값..^^ 
result = solution(string)
print(result)