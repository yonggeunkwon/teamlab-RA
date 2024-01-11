db = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]
id_pw = ["prograr01", "111111"]

answer = ''

for i in range(len(db)):

    if id_pw == db[i]: # db의 list중 id_pw와 일치한게 있다면
        answer = 'login'
        break
    if id_pw[0] == db[i][0]: # 아이디만 일치하다면
        answer = 'wrong pw'
        break
    else :
        answer = 'fail'

print(answer)