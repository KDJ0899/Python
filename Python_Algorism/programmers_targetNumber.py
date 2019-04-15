'''
Created on 2018. 10. 8.

@author: user
'''
def solution(numbers, target):
    answer = 0
    answer=targetNumber(numbers, target, 0)
    return answer

def targetNumber(numbers,target,i):
    if i==len(numbers):
        if target==0:
            return 1
        return 0
    return targetNumber(numbers,target-numbers[i],i+1)+targetNumber(numbers, target+numbers[i], i+1)
print(solution([1,1,1,1,1],3))