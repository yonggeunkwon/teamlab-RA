def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
    return answer

my_str = "abc1Addfggg4556b"
n = 6
result = solution(my_str, n)
print(result)

# 오답코드01
# def solution(my_str,n):
#     # 1번째 문자부터 n번째 문자까지 자르기 -> 문자열 슬라이싱
#     # n+1번째 문자부터 2n번째 문자까지 자르기 -> 그럼 인덱스는 어떻게 되나
#     for i in range(0,len(my_str),n):
#         result = my_str[i:i+n]
#         print(result)
#         # 이렇게만 하면 마지막 i가 결국 12라 my_str[12:18]이 반환됨
#     return result


# 오답코드02
# def solution(my_str,n):
#     for i in range(0,len(my_str),n):
#         answer = []
# # 반복문 안에서 answer를 생성하는 바람에, i가 결정될 때마다(반복문이 돌 때마다) answer 리스트가 매번 업데이트 됨
# # 누적되지 않고 매번 업데이트 된다는 문제 (누적시키려면 for문 밖에서 빈 리스트 만들기)
#         answer.append(my_str[i:i+n])
#         print(answer)
#     return answer

# my_str = "abc1Addfggg4556b"
# n = 6
# result = solution(my_str,n)
# print(result)
