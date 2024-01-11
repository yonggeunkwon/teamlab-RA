def solution(my_str):
    answer = []  # 리스트 초기화
    word = ""  # 임시 문자열 선언
    for i in my_str:
        word += i
        if len(word) == n:  # 임시 문자열의 길이가 n과 같아졌을 때
            answer.append(word)
            word = ""
    if word != "":  # 임시 문자열이 비어있지 않다면
        answer.append(word)
    return answer


if __name__ == "__main__":
    my_str = "abc1Addfggg4556b"
    n = 6
    result = solution(my_str)
    print(result)