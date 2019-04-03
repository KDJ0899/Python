'''
트리를 만들고 후위순회를 하여 런타임 에라가 남
Created on 2018. 7. 23.

@author: user
'''
class tree:
    x=0
    def __init__(self,x):
        self.x=x
        self.left=tree
        self.right=tree

def LeftSearch(root,x):
    if(root.x<x):
        RightSearch(root, x)
    else:
        if(root.left.x==0):
            new_tree=tree(x)
            root.left=new_tree
        else:
            LeftSearch(root.left, x)

def RightSearch(root,x):
    if(root.x>x):
        LeftSearch(root, x)
    else:
        if(root.right.x==0):
            new_tree=tree(x)
            root.right=new_tree
        else:
            RightSearch(root.right, x)

def postfix(root):
    if(root.left.x!=0):
        postfix(root.left)
    if(root.right.x!=0):
        postfix(root.right)
    print(root.x)
        
x=int(input())
root=tree(x)
while(1):
    x=int(input())
    if(x==-1):
        break
    if(x<root.x):
        LeftSearch(root, x)
    else:
        RightSearch(root, x)
postfix(root)  
    