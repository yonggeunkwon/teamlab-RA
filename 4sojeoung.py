# 모음 제거

# moumm = ['a','e','i','o','u']

# def solution():
#     my_string = "bus"
#     for i in my_string:
#         if i in moumm:
#             my_string = my_string.replace(i,'')
#     return my_string

# print(solution())
#파이썬 함수 내에서 전역 변수를 수정하려면 global 키워드를 통해서 전역변수임을 명시

my_string = "bus"
# [lambda my_string : ''.join(i) for i in my_string if i not in 'aeiou']
f = ''.join([i for i in my_string if i not in 'aeiou'])
print(f)