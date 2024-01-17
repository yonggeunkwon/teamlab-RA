def solution(s) :

    lower_s = s.lower()
    print(lower_s)

    #변수s 속에 있는 p와 y의 개수 알기
    count_p = lower_s.count("p")
    count_y = lower_s.count("y")

    print(count_p)
    print(count_y)

    #p와 y의 개수가 같다면 True (p, y가 없는 경우도 항상 True)
    if count_p == count_y :
        return True
    #p와 y의 개수가 다르다면 False
    elif count_p != count_y :
        return False

s = "pPoooyY"
print(solution(s))