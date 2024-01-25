# 문자열 겹쳐쓰기

my_string = 'He11oWorld'
overwrite_string = 'lloWorl'
s = 2

my_string_list = list(my_string)

def sol():
    my_string_list[s:s+len(overwrite_string)] = overwrite_string
    result = ''.join(my_string_list)
    return result

print(sol())

# 디버그 -> 빨간점 누르고 fn키와 f5
# 리스트로 쪼개서 다시 풀어보기 -> 한글자면 오류 남