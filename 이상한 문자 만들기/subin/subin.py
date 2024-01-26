s = " try hello world"
split_s = s.split(" ")
print(split_s)

result = ""
for i in split_s :
    result += " "   
    #의도: 한 리스트를 돌리면서 공백을 채워주는 걸 생각하면서 작성했는데, 
    #첫번째 공백이 생길거라는 생각을 못 함. 그래서 예... 난관에 봉창했다..ㅎㅎ
    for index, j in enumerate(i):
        print(index, j)
        if index % 2 == 0 :
            a = j.upper()
            result += a 
        elif index % 2 != 0 :
            b = j.lower()
            result += b
        #print(result.lstrip())
        # 한단어가 끝나면 공백 넣어주기...
print(result[1:])    # ㅋ 질문하기 보다가 알았어요 ^.^

##질문: 왜 lstrip()을 사용하면 왜 테스트가 통과가 안 되나요?

#굳이 리스트에 넣어주지 말고 string 자체로 문제 풀어서 합쳐주기.