my_str='abc1Addfggg4556b'
n=6

new_list = [my_str[i:i+n] for i in range(0,len(my_str),n)]

print(new_list)