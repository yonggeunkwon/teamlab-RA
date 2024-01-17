my_string = "hello"
n = 3
#list로..
my_list = list(my_string)
result = ""
#n개씩 문자들이 나오도록 ex) h, h, h, e, e, e 이런식으로
for i in range(len(my_string)) :
    #print(i)
    #각각의 인덱싱을 n으로 곱해주기
    #print(my_list[i])
    a = my_list[i]*n
    print(a)
    #합쳐주기 #힌트 ...
    result += a #이 한 줄 !!