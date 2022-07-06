
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

BT = BinaryTree(size=8)
print(BT.insertNode("Gadgets"))
print(BT.insertNode("Ipad"))
print(BT.insertNode("Mobile"))
print(BT.insertNode("IpadEarphone"))
print("####")
print(BT.searchNode("Mobile"))

