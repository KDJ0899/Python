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
    for z in range(k+1):#z�� ����
        for x in range(n):#x�� ȣ��
            if z==0:
                arr[x]=x+1#z�� 0���϶� xȣ���� x���� ��.
                continue
            else:
                if x==0:
                    newarr[x]=1#������� 0ȣ�� 1��
                else:
                    newarr[x]=arr[x]+newarr[x-1]#�������� ��ȣ(newarr[x-1])���� ���� x-1ȣ ���� ��� ���� ���� ����ֱ� ������ ������ xȣ�� ���� �����ָ� ��.
        if(z!=0):
            arr=newarr
    print(arr[n-1])