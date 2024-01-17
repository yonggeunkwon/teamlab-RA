def solution (quiz) :
    
    result_list = []
    for expression in quiz :
        list = expression.split(" ")   #list[0]의 자료형은 string임.. 계산할 수 있게 바꿔야함
        X = list[0]
        Y = list[2]
        Z = list[4]

        if int(X) + int(Y) == int(Z) :   #식 계산
            result_list.append("O")
        
        elif int(X) - int(Y) == int(Z) :    #식 계산
            result_list.append("O")

        else :           #if문 만족안하면
            result_list.append("X")
    
    return result_list

quiz = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]
print(solution(quiz))