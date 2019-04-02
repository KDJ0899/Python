'''
BaekJoon_2775 Success
Created on 2018. 7. 17.

@author: user
'''

a=int(input())
arr=[None]*14
newarr=[None]*14
for i in range(a):
    k=int(input())
    n=int(input())
    for z in range(k+1):#z는 층수
        for x in range(n):#x는 호수
            if z==0:
                arr[x]=x+1#z가 0층일때 x호에는 x명이 삼.
                continue
            else:
                if x==0:
                    newarr[x]=1#모든층에 0호는 1명
                else:
                    newarr[x]=arr[x]+newarr[x-1]#같은층에 전호(newarr[x-1])에는 전층 x-1호 까지 모두 더한 값이 들어있기 떄문에 전층에 x호의 값만 더해주면 됨.
        if(z!=0):
            arr=newarr
    print(arr[n-1])