'''
 Creation of Binary Tree using Linked List
 - Creation of Tree
 - Insertion of a node
 - Deletion of a node
 - Search for a value
 - Traverse all nodes -> 4 ways of traversing
 - Deletion of tree

 * Traversal of Binary Tree
    - Depth First Search
        - Preorder traversal
        - Inorder traversal
        - Post order traversal
    - Breadth first search
        - Level order traversal
 '''

from QueueLinkedList import Queue


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None


BT = TreeNode("Gadgets")
leftChild = TreeNode("IPad")
leftChild.leftChild = TreeNode("IPadCharger")
leftChild.rightChild = TreeNode("IPadEarphone")
rightChild = TreeNode("Mobile")
rightChild.rightChild = TreeNode("MobileCharger")
BT.leftChild = leftChild
BT.rightChild = rightChild


# Time: O(n) ; Space: O(n)
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# Time: O(n); Space: O(n)
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# Time: O(n); Space: O(n)
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# Time: O(n); Space: O(n)
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

# Time: O(n); Space: O(n)
def searchValueBT(rootNode, nodeValue):
    if not rootNode:
        return "The Binary Tree does not exist"
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Value found Sucessfully!"

            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Value not found!"

# Insert a node in Binary Tree
# we do level order traversal to insert node 
# Since it is queue and it is efficient than recursion(PreOrder, InOrder, PostOrder)
# Case1: A root node is blank
# Case2: The tree exists and we have to look for a first vacant place
# Time: O(n); Space: O(n)
def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "New Value inserted sucessfully!"
           
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "New Value inserted sucessfully!"

def getFarthestNode(rootNode):
    # Time: O(n); Space: O(n)
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        # the last node is farthest among all
        return root.value

def deleteFarthestNode(rootNode, fNode):
    # Time: O(n); Space: O(n)
    if not rootNode:
        return 

    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()

            if root.value is fNode:
                root.value = None
                return 
            if root.value.rightChild:
                if root.value.rightChild is fNode:
                    root.value.rightChild = None
                    return 
                else:
                    customQueue.enqueue(root.value.rightChild)

                if root.value.leftChild:
                    if root.value.leftChild is fNode:
                        root.value.leftChild = None
                        return 
                    else:
                        customQueue.enqueue(root.value.leftChild)

def deleteNodeBT(rootNode, node):
    # We use LevelOrderTraversal to search node
    # If we found the node to delete
    # We get the farthest node and
    # Replace node to delete with farthest node
    # And delete farthest node
    # Note: We can't directly delete the given node since
    #       Other nodes linked with it also gets deleted
    # Time: O(n); Space: O(n)
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getFarthestNode(rootNode)
                root.value.data = dNode.data
                deleteFarthestNode(rootNode, dNode)
                return "The node has been sucesfully deleted"
            
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete"

def deleteEntireBT(rootNode):
    # We have implemented BT with linked list
    # Simply make rootNode -> None
    # And left child and right child of rootNode both -> None
    # This will delete entire BT by garbage collector
    # Time: O(1); Space: O(1)
    if not rootNode:
        return "The BT does not exist"
    
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None

    return "Sucessfully deletion of entire BT."

preOrderTraversal(BT)
print("###########")
inOrderTraversal(BT)
print("#######")
postOrderTraversal(BT)
print("############")
levelOrderTraversal(BT)
print("##########")
print(searchValueBT(BT, "MobileCharger"))
print("##########")
# Insert new node in BT
newNode = TreeNode("MobileEarphone")
print(insertNodeBT(BT, newNode))
levelOrderTraversal(BT)
print("#########")
farthestNode = getFarthestNode(BT)
print(farthestNode.data)
print("######")
# deleteFarthestNode(BT, farthestNode)
# levelOrderTraversal(BT)
# print("####")

deleteNodeBT(BT, 'Mobile')
levelOrderTraversal(BT)
# Deletion of Entire BT
print("##########")
deleteEntireBT(BT)
levelOrderTraversal(BT)
