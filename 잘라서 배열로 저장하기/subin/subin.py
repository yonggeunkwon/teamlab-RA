##슬라이싱과 리스트를 이용해서 풀기 !!
#정답나왔찌롱 ~~~~ ^^v 

my_str = 'abc1Addfggg4556b'

#몇 개씩 나눌 것인지
n = 6

#인덱스를 뽑아서.. ^^
for index, i in enumerate(my_str) :
    print(index, i)
    
    #여기서 인덱스를 n개씩 자르기(슬라이싱사용)
    result = []
    for j in range(0, len(my_str), n) :  #시작하는 인덱스에서 끝나는 인덱스까지 6개씩 증가.
        a = result.append(my_str[j:j+n])
        print(result)