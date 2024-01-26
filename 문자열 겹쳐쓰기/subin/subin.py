def solution(my_string, overwrite_string, s) :
    a = len(overwrite_string)

    list_my_string = list(my_string)
    del(list_my_string[s:s+a])

    for i in overwrite_string :
        if list_my_string != [] :
            list_my_string[s-1] += i
        else :
            list_my_string += i

    str_my_list = "".join(list_my_string)
    return str_my_list

my_string = "a"
overwrite_string = 	"b"
s = 0
print(solution(my_string, overwrite_string, s))