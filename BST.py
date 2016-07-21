'''
Created on Jul 20, 2016

@author: subham
'''






class BSTNode():

    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None
    
    
class BST():
    
    def __init__(self,node=None):
        self.root = node
        
        



def inorderwalk(root):
    if root:
        inorderwalk(root.left)
        print(root.key)
        inorderwalk(root.right)
        
        
        


def preorderwalk(root):
    if root:
        print(root.key)
        preorderwalk(root.left)
        
        preorderwalk(root.right)

def postorderwalk(root):
    if root:
        
        postorderwalk(root.left)
        
        postorderwalk(root.right)
        print(root.key)
        
        
def bst_search(root,key):
    if root==None or root.key==key:
        return root
    elif root.key>key:
        return bst_search(root.left,key)
    else:return bst_search(root.right,key)
        
def getMin(root):
    while root.left!=None:
        root=root.left
    return root  

def getMax(root):
    while root.right!=None:
        root=root.right
    return root  

def getmax_recursive(root):
    if root.right!=None:
        return getmax_recursive(root.right)
    return root 


def getmin_recursive(root):
    if root.left!=None:
        return getmin_recursive(root.left)
    return root  

def successor(node): 
    if node.right:
        return getMin(node.right)
    else:
        parent_node=node.parent
        while parent_node and node==parent_node.right:
            node = parent_node
            parent_node = node.parent
        return parent_node
    
    
    
       
def predecessor(root):
    if root.left!=None:
        return getMax(root.left)
    else:
        parent_child = root.parent
        while parent_child and  root == parent_child.left:
            root = parent_child
            parent_child = parent_child.parent
        return parent_child
    
    


def insert(tree,key):
    node = BSTNode(key)
    prev = None
    ptr = tree.root
    #print(ptr)
    while ptr!=None:
        prev = ptr
        if ptr.key>node.key:
            ptr = ptr.left
        else:
            ptr=ptr.right
    node.parent = prev
    
    if prev==None:
        tree.root = node
    
    elif prev.key>node.key:
        prev.left=node
    else:
        prev.right=node
     

tree = BST()

insert(tree,7)
insert(tree,5)
insert(tree,3)
insert(tree,2)
insert(tree,6)
insert(tree,8)
insert(tree,9)




print(inorderwalk(tree.root))
