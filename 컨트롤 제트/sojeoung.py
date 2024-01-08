# s="1 2 Z 3"
# new=list(s.split())
# f_list=[]

# for i in range(len(new)):
#     if i+1>=len(new):
#         break
#     elif new[i+1] == 'Z':
#         new[i]=''
#         new[i+1]=''

# if new[i].isdigit() == True:
#     f_list.append(int(new[i])) 

# q=sum(f_list)
# print(q)

## stack & pop 사용해서 풀어보기

s='1 2 Z 3'
stack=[]

for i in s:
    if i.isdigit():
        stack.append(int(i))
    elif i == 'Z' :
        f=stack.pop()

result=sum(stack)
print(result)