class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sum_values(root):
    if (root == None):
        return 0
    return root.data + sum_values(root.left) + sum_values(root.right)


#  Our example tree looks like this:
#         2
#       /   \
#      3     4
#     / \
#    5   6

node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node2.left = node3
node2.right = node4
node3.left = node5
node3.right = node6

print("Sum of all values of this tree is (should print 20):")
print(sum_values(node2))

+____________________________________________________________________________________________________________________________________________________________________
class Node :
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
sums=[]

def prin(node,current):
    if node==None:
        # print(sums)
        return
    
    currentsum=current+node.data
    
    print("node here is : ",node.data,"sum here is : ",currentsum)
    
    if node.left is None and node.right is None:
        sums.append(currentsum)
        
    prin(node.left,currentsum)
    # print(node.data,end=" ")
    prin(node.right,currentsum) 
    
root=Node(2)
root.left=Node(3)
root.right=Node(4)
root.left.left=Node(5)
root.left.right=Node(6)

prin(root,0)

__________________________________________________________________________________________________________________________________________________________________


class Node :
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data,end=" ")
    inorder(node.right)
    
root=Node(10)
root.left=Node(5)
root.right=Node(15)
root.left.left =Node(2)
root.left.left.left =Node(1)
root.left.right=Node(5)
root.right.right=Node(22)
root.right.left=Node(13)
root.right.left.right=Node(14)
inorder(root)
finding(root,target)

___________________________________________________________________________________________________________________________________________________________________


showing , searching and inserting in BST : 

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def show(root):
    if root is None :
        return 
    print("data is : ",root.data)
    show(root.left)
    show(root.right)
    
def insert(value,root):
    if root is None:
        return
    print(" current value is : ",root.data)    
    if root.left is None or root.right is None:
        node9 = Node(value)
        root.right = node9
        print("got it ")
        return
    if root.data > value :
        insert(value,root.left)
    elif root.data < value : 
        insert(value,root.right)
        
node1 =  Node(4)
node2 =  Node(2)
node3 =  Node(1)
node4 =  Node(3)
node5 =  Node(6)
node6 =  Node(5)
node7 =  Node(7)

node1.left = node2
node1.right = node5
node2.left = node3
node2.right = node4
node5.left = node6
node5.right = node7

print(show(node1))
print(insert(8,node1))
print(show(node1))
_____________________________________________________________________________________________________________________________________________________________
        
        