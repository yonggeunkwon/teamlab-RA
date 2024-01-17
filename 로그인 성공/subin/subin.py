id_pw =["programmer01", "15789"]
db = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]
for i in db :
    print(i)
    if i[0] != id_pw[0] :
        print("fail")
    elif i[0] == id_pw[0] and i[1] == id_pw[1] :
        print("login")
    elif i[0] == id_pw[0] and i[1] != id_pw[1] :
        print("wrong pw")