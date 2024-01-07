def solution(my_string):
    answer = []

    for i in my_string:
        if i.isdigit():  # 문자가 숫자인 경우에만
            answer.append(int(i))  # 문자를 정수로 반환하여 리스트에 추가

    answer.sort()  # 리스트 오름차순 정렬
    return answer


if __name__ == "__main__":
    my_string = "hi12392"
    result = solution(my_string)
    print(result)
