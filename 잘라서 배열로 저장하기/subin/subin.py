##슬라이싱과 리스트를 이용해서 풀기 !!

my_str = 'abc1Addfggg4556b'

#몇 개씩 나눌 것인지
n = 6

my_list = []
for i in my_str :
    my_list.append(i)
print(my_list)

result = []
for char in range(0, len(my_list), n) :
    result.append(my_list[char:char+n])   #요부분이 pOinT같음 ㅇㅇ!
print(result)

for list in result :
    print(list)

#결과값이 이렇게 나오는데.. 
#['a', 'b', 'c', '1', 'A', 'd']
#['d', 'f', 'g', 'g', 'g', '4']
#['5', '5', '6', 'b']
#리스트 속 문자열을 합치고 싶어요.. (일단 시도들은 해보았지만.. ㄴㄴ임니다..)