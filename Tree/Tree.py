 

 

class TreeNode:
    def __init__(self, data, children=[]) -> None:
        self.data = data
        self.children = children
    
    def __str__(self, level=0) -> str:
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)
    

tree = TreeNode('Gadgets', [])
Ipad = TreeNode('Ipad', [])
mobile = TreeNode('Mobile', [])
tree.addChild(Ipad)
tree.addChild(mobile)

IpadCharger = TreeNode('IpadCharger', [])
mobileCharger = TreeNode('MobileCharger', [])
Ipad.addChild(IpadCharger)
mobile.addChild(mobileCharger)
print(tree)

