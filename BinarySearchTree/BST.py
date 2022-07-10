

'''
Traversal of Binary Search Tree

Depth First Search
  - Preorder traversal
  - Inorder traversal
  - Postorder traversal

Breadth first search
   - Level order traversal
'''

from QueueLinkedList import Queue

class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

# Time: O(logn); Space: O(logn)
# Insert a value in Binary Search Tree
# We search for a empty space and insert a value that
# satisfy the properties of Binary Search Tree
def insertNode(rootNode, nodeValue):
        if rootNode.data is None:
            rootNode.data = nodeValue
        elif nodeValue <= rootNode.data:
            if rootNode.leftChild is None:
                rootNode.leftChild = BSTNode(nodeValue)
            else:
                insertNode(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild is None:
                rootNode.rightChild = BSTNode(nodeValue)
            else: 
                insertNode(rootNode.rightChild, nodeValue)

        return "The node has been successfully inserted"

# Traversal of Binary Search Tree

# PreOrder Traversal of BST
# 1. Visit Root Node -> LeftSubTree -> RightSubTee
# Time: O(n); Space: O(n)
def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data, end='->')
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# Inorder Traversal of BST
# Vist LeftSubTree -> RootNode -> RightSubTree
# Time: O(n); Space: O(n)
def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end='->')
    inOrderTraversal(rootNode.rightChild)

# PostOrder Traversal of BST
# Visit LeftSubTree -> RightSubTree -> RootNode
# Time: O(n); Space: O(n)
def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data, end='->')

# Breadth Fist Search -> Level Order Traversal
# Time: O(n); Space: O(n)
def levelOrderTraversal(rootNode):
    if not rootNode:
        return 
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data, end='->')
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

# Search for a node in Bineary Search Tree
# Time: O(logn); Space: O(logn)
def searchNode(rootNode, nodeValue):
    if rootNode is None:
        return 
    if rootNode.data == nodeValue:
        print("Value found!")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild is not None:
            if rootNode.leftChild.data == nodeValue:
                print("Value found!")
            else:
                searchNode(rootNode.leftChild, nodeValue)
        else:
            print("Value not Found!")
    else:
        if rootNode.rightChild is not None:
            if rootNode.rightChild.data == nodeValue:
                print("Value Found!")
            else:
                searchNode(rootNode.rightChild, nodeValue)
        else:
            print("Value not Found!")


def minValueNode(curNode):
    # minimum value lie in leftchild of current node
    current = curNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current

# Delete a node from Binary Search Tree
# Three cases:
# Case1: The node to be deleted is a leaf
# Case2: The node has one child
# Case3: The node has two children 
#   In this we have to find successor, which is minimum
#   value of rightSubTree. So, min Value is new parent node
#   where the value gets deleted.
# Time: O(logn); Space: O(logn)
def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild= deleteNode(rootNode.rightChild, temp.data)
    return rootNode

# TIme: O(1); Space: O(1)
def deleteEntireBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been successfully deleted"





newBST = BSTNode(None)
print(insertNode(newBST, 70))
print(insertNode(newBST, 50))
print(insertNode(newBST, 90))
print(insertNode(newBST, 30))
print(insertNode(newBST, 60))
print(insertNode(newBST, 80))
print(insertNode(newBST, 100))
print(insertNode(newBST, 20))
print(insertNode(newBST, 40))

'''
Binary Search Tree looks like as:
Must Satisfy two properties:
-	In the left subtree the value of a node is less than or equal to its parent node’s value.
-	In the right subtree the value of a node is greater than its parent node’s values.


                                70
                               /  \
                              /    \
                             50     90
                            /  \    /  \
                           30  60   80  100
                          /  \
                         20  40

'''

print("###")
preOrderTraversal(newBST)
print("\n##")
inOrderTraversal(newBST)
print("\n##")
postOrderTraversal(newBST) 
print("\n##")
levelOrderTraversal(newBST)
print("\n##")
searchNode(newBST, 60)
searchNode(newBST,  10)
deleteNode(newBST, 60)
levelOrderTraversal(newBST)
print("##")
print(deleteEntireBST(newBST))
levelOrderTraversal(newBST)