class BST():

    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None



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
        

root = BST(5)
node1 = BST(3)

node2 = BST(7)

node3 = BST(2)

node4 = BST(5)
node5 = BST(8)

root.left=node1
node1.parent=root

root.right=node2
node2.parent=root


node1.left = node3
node3.parent=node1

node1.right = node4
node4.parent=node1

node2.right = node5
node5.parent=node2

postorderwalk(root)




