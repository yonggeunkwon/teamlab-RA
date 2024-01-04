# write code
## 소정이가 쓴 코드

def solution(my_string):
    if 1<=len(my_string)<=1000: #제안1
        plus_result=[]

        for i in my_string:
            if i.isdigit() == True and 1<=int(i)<=1000: #제안2,4
                plus_result.append(i)
            else:
                plus_result.append('_')
        
        for i in range(len(plus_result)):
            if i+1>=len(plus_result):
                break
            elif plus_result[i].isdigit()==True and plus_result[i+1].isdigit()==True:
                x = plus_result[i],plus_result[i+1]
                z=''.join(x) #제안3
                plus_result[i+1]=z
                plus_result[i]='_'
        print(plus_result)
        
        result_list=[]
        for i in range(len(plus_result)):
            if plus_result[i].isdigit():
                result_list.append(int(plus_result[i]))
        print(result_list)
    
    answer = sum(result_list)
    return answer

if __name__=="__main__":
    my_string='aAb1B2cC34oOp'
    result = solution(my_string)
    print(result)