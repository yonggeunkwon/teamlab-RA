#ㅋㅋㅋ레알 어거지... 씨붕 ㅋㅋ 꾸역꾸역 ㅠ^ㅠ
#최선입니다.. ㄹㅇ 이 이상 난 모태..yo.ㅠㅠb
#프로그래머스에 돌리니까 모든 예시의 결과값은 나오는데
#제출하려고 하니까 틀렸어요.^^!

s = "1 2 Z 3"  #공백제거해줘야함
split_s = s.split(" ")

list = []
for i in split_s :
    list.append(str(i))
print(list)

#범위를 설정해서 "Z"를 앞 숫자와 동일하게 바꿔줌.
for j in range(len(list)) :
    if list[j] != "Z" :       #"Z"가 아니라면 pass
        pass
    else :                    #"Z"라면 앞 숫자와 같게 변경시켜줌        
        list[j] = list[j - 1] # 여기서 마이너스 부호를 붙이고 싶음.ㅠbㅠ
print(list)

#중복되는 수가 있다면 두 수 모두 0으로 바꾸기 (우겨넣어서 만들기 ^^b, 지송함니다..HaHA..)
for k in range(len(list)) :
    if list[k] == list[k - 1] :
        list[k] = 0
        list[k - 1] = 0
print(list)

#문자열을 정수로 변경한 뒤 더해주기
last_list =[]
for n in list :
    last_list.append(int(n))
    sum_list = sum(last_list)
print(sum_list)