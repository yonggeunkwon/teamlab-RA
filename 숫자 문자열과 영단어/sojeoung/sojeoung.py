# 숫자 문자열과 영단어

s = "one4seveneight"
num_alpha = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

for key, value in num_alpha.items():
    s = s.replace(key, str(value))

print(s)

# 01. 딕셔너리에 넣기
# 02. 반복문에 문자열 넣기
# 03. 문자 하나씩 더할 때 마다 검사해서 딕셔너리 keys 안에 있으면 변환 ! + 초기화 해주기

# 01. items로 키랑 밸류를 꺼내서 replace로 바꾸기 (대신 스트링으로 바꾸기)