# 소수 만들기

from itertools import combinations

nums = [1,2,3,4]

def solution(nums):
    char = 0
    memo = []
    
    for c in combinations(nums,3):
        plus_c = sum(c)
        for x in range(2,plus_c):
            if (plus_c) % x != 0:
                memo.append(0)
            else:
                memo.append(1)
        if 1 not in memo:
            char += 1
        memo = [] ## 초기화
    return char

print(solution(nums))