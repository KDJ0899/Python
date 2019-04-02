'''
BaekJoon_2490 Success
Created on 2018. 7. 23.

@author: user
'''
arr=[None]*4
for i in range(3):
    x=0
    y=0
    k=input()
    arr=k.split(" ")
    for j in range(4):
        if(arr[j]=='0'):
            x+=1
        else:
            y+=1
    if(x==1):
        print('A')
    elif(x==2):
        print('B')
    elif(x==3):
        print('C')
    elif(x==4):
        print('D')
    else:
        print('E')
        
    