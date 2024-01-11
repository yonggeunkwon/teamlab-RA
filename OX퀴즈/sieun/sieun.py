quiz = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]
answer = []

for i in quiz:
    array = i.split(" ")
    
    # 연산자와 피연산자 따로 저장
    left = int(array[0])
    operator = array[1]
    right = int(array[2])

    if operator == '+': # 연산가 + 일 때 
        result = left + right 
    elif operator == '-': # 연산자가 - 일 때
        result = left - right

    if result == int(array[4]): # result가 결과값과 동일하다면 
        answer.append("O") # answer list에 O 추가 
    else: # 동일하지 않다면
        answer.append("X")

print(answer)