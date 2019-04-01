'''
BaekJoon_2161 Success
Created on 2018. 7. 19.

@author: user
'''
n=int(input())
arr=[]
for i in range(n):
    arr.append(i+1)
for i in range(n-1):
    print(arr.pop(0))
    a=arr.pop(0)
    arr.append(a)
print(arr.pop(0))