
"Creation of Binary Tree using Python List"
class BinaryTree:
    def __init__(self, size) -> None:
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
    def insertNode(self, value):
        #  Two Case: Either BT is full or there is vacant place to insert new node
        # We use level order traversal to search for the first vacant place.
        # And add using lastUsedIndex
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"
    
    def searchNode(self, nodeValue):
        # Search through the list
        # if found return Sucess message
        # TIme: O(n); Space: O(1)
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Value not found"
    
    def preOrderTraversal(self, index):
        '''
        index: is the position where we start to place node value
        In PreOrder:
            RootNode => LeftSubTree => RightSubTree
        Time: O(n); Space: O(n)
        '''
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)
    
    def inOrderTraversal(self, index):
        '''
        In InOrder:
            LeftSubtree => RootNode => RightSubTree
        '''
        if index > self.lastUsedIndex:
            return 
        
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2 + 1)

    def postOrderTraversal(self, index):
        '''
        In PostOrder:
            LeftSubTree => RightSubTree => RootNode
        Time: O(n); Space: O(n)
        '''
        if index > self.lastUsedIndex:
            return 
        
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index*2 + 1)
        print(self.customList[index])

    # Time: O(n); Space: O(1)
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

    # Delete a node from a Binary Tree
    # Steps:
    # 1. deepest node is lastusedIndex
    # 2. Replace the node to be delete by deepest node 
    # 3. Delete a deepest node from binary tree
    # Time: O(n); Space: O(1)
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been sucessfully deleted"
    
    def deleteEntireBT(self):
        # set customList to None which will erase entire binary tree
        # Time: O(1); Space: O(1)
        self.customList = None
        return "The BT has been sucessfully deleted"



BT = BinaryTree(size=8)
print(BT.insertNode("Gadgets"))
print(BT.insertNode("Ipad"))
print(BT.insertNode("Mobile"))
print(BT.insertNode("IpadEarphone"))
print(BT.insertNode("MobileEarphone"))
print(BT.customList)
'''

        Gadgets(1)
        /        \
       Ipad(2)    Mobile(3)
    /          \
   /            \
IpadEarphone(4)  MobileEarphone(5)

In python list looks as:
[None, 'Gadgets', 'Ipad', 'Mobile','IpadEarphone', 'MobileEarphone', None, None]
Note: index is the position where we start to place node value
Use formula: LeftChild = 2*index
             RightChild = 2*index + 1

'''
print("####")
print(BT.searchNode("Mobile"))
print("####")
BT.preOrderTraversal(1)
"Output: Gadgets -> Ipad -> IpadEarphone -> MobileEarphone -> Mobile"
print("###")
BT.inOrderTraversal(1)
"Output: IpadEarphone -> Ipad -> MobileEarphone -> Gadgets -> Mobile"
print("###")
BT.postOrderTraversal(1)
"Output: IpadEarphone ->  MobileEarphone -> Ipad -> Mobile-> Gadgets"
print("###")
BT.levelOrderTraversal(1)
print("####")
BT.deleteNode("MobileEarphone")
BT.levelOrderTraversal(1)
print(BT.deleteEntireBT())