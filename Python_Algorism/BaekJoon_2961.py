'''
BaekJoon_2961 Success
Created on 2018. 7. 19.

@author: user
'''
def Recursion(i,x,y):
    global least
    x*=int(arr[i][0])
    y+=int(arr[i][1])
    sub=abs(x-y)
    print(i,x,y)
    if(least>=sub):
        least=sub
    for a in range(i+1,n,1):
        Recursion(a,x,y)    
least=1000000000
x=1
y=0
n=int(input())
arr=[[0]*2 for i in range(n)]
for i in range(n):
    st=str(input())
    arr[i]=st.split(" ")
for i in range(0,n,1):
    Recursion(i, x, y)
print(least)