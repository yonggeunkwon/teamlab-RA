id_pw = ["meosseugi", "1234"]
db = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]

def solution(id_pw,db):
    if id_pw in db:
        return "login"

    for i in db:
        if id_pw[0] == i[0]:
            if id_pw[1] != i[1]:
                return 'wrong pw'
        else:
            return "fail"
            break
print(solution(id_pw, db))