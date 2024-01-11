# (2) stack 이용해서 풀어보기 (pop함수) 
    # └ list에 제일 마지막 들어간 걸 빼주는 거
s = "1 2 Z 3"
split_s = s.split(" ")

list=[]
for char in split_s :
    if char.isdigit() == True : # 숫자가 맞다면 list에 숫자를 추가 
        list.append(int(char))
    else :                      # 숫자가 아니라면 마지막에 들어간 숫자 빼주기 
        list.pop()              # 요래 쓰는 게 맞나요..?
#print(list)

sum_list = sum(list)
print(sum_list)