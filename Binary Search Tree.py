class Node:

    def __init__(self,value):
        self.left=None  #left child
        self.right=None #right child
        self.value=value #Node value



class Tree:

    #Constructor for BST
    def __init__(self):

        self.root=None #set root as null  initially 

    def addNode(self,node,value):
        if None == node:
            newNode = Node(value)
            return newNode
        
        if value<node.value:
            node.left = self.addNode(node.left,value)
        else:
            node.right = self.addNode(node.right,value)


    def printInorder(self,node):
        if node:
            self.printInorder(node.left)
            print(node.value)
            self.printInorder(node.right)
            




bst1 = Tree()
bst1.root = bst1.addNode(bst1.root,1)
bst1.root = bst1.addNode(bst1.root,8)
bst1.root = bst1.addNode(bst1.root,5)

bst1.printInorder(bst1.root)