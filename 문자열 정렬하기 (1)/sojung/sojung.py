def solution(my_string):
    answer=[]
    for i in my_string:
        if i.isdigit()==True:
            answer.append(int(i))
    return sorted(answer)

my_string='hi12392'
result = solution(my_string)
print(result)

## 스트링 값은 반복문에 그대로 넣을 수 있다 -> list 변환 필요 X
## 그냥 넘어가는 것 -> pass