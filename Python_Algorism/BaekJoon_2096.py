'''
Created on 2018. 10. 8.

@author: user
@comment: 백준 2096번 내려가기 문제 풀이
'''
# def Recursion(i,j,sumval):
#     global maxval,minval
#     sumval+=int(arr[i][j])
#     if i==n-1 :
#         if(sumval>maxval):
#             maxval=sumval
#         if(sumval<minval):
#             minval=sumval
#         return
#     if j!=0:
#         Recursion(i+1, j-1, sumval)
#     Recursion(i+1, j, sumval)
#     if j!=2:
#         Recursion(i+1, j+1, sumval)
    
n=int(input())
maxarr=[0]*6
minarr=[0]*6
arr=[0]*3

for i in range(0,n):
    arr=[int (x)for x in input().split(" ")]
    maxarr[0]=max([maxarr[3],maxarr[4]])+arr[0]
    maxarr[1]=max([maxarr[3],maxarr[4],maxarr[5]])+arr[1]
    maxarr[2]=max([maxarr[4],maxarr[5]])+arr[2]

    minarr[0]=min(minarr[3],minarr[4])+arr[0]
    minarr[1]=min(minarr[3],minarr[4],minarr[5])+arr[1]
    minarr[2]=min(minarr[4],minarr[5])+arr[2]
    
    for j in range(3):   
        maxarr[j+3]=maxarr[j]
        minarr[j+3]=minarr[j]
maxval=max(maxarr[0],maxarr[1],maxarr[2])
minval=min(minarr[0],minarr[1],minarr[2])
print(maxval,minval)
        

    