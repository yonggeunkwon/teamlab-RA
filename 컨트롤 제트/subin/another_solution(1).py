# (1) 용근님 - Z기준으로 없으면 숫자 더해, 있으면 앞에 숫자 빼줘.
## 아 그런데 이거 완전 이해 ㄴㄴ..

s = "1 2 Z 3"
split_s = s.split(" ")

answer = 0 #여기 변수에 숫자들을 더해주기(아 그러니까 더해준 숫자들을 반환?)

for char in split_s :
    if char != "Z" :          # 1. "Z"가 없다면
        number = int(char)    # 정수를 number라는 변수에 할당.
        answer += number      # 증가연산
    elif char == "Z" :        # 2. "Z"가 있다면
        answer -= number      # 감소연산 ("Z" 앞 숫자들을 빼주기)
print(answer) 