

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
    
    # Creation of circular singly linked list
    def createCSLL(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node

    # Insertion in circular singly linked list
    def insertInCSLL(self, value, location):
        if self.head is None:
            return
        else:
            newNode = Node(value)
            # Insert at first -> TIme: O(1); Space: O(1)
            # 1. Update newNode.next = head
            # 2. Update lastNode.next -> newNode
            # 3. Update tail to newNode
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                lastNode = self.tail
                lastNode.next = newNode

            # Insert into last -> Time: O(1); Space: O(1)
            # 1. Update last node next = newNode
            # 2. Update newNode.next = reference to first node
            # 3. Update tail to newNode
            elif location == -1:
                prevNode = self.tail
                prevNode.next = newNode
                newNode.next = self.head
                self.tail = newNode
            
            else:
                # Insert into kth location -> Time: O(n); Space: O(1)
                # 1. Traverse to k-1 node
                # 2. Update newNode next to k-1 node.next
                # 3. Update k-1 node.next to newNode

                # 1. Traverse to k-1 node; where k is the position to insert newNode
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                # 2. Update newNode next to k-1 node.next
                newNode.next = tempNode.next
                # 3. Update k-1 node.next to newNode
                tempNode.next = newNode

    # Time: O(n)
    def traversalCLL(self):
        if self.head is None:
            print("No any node to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
    
    # Searching for a node in circular singly linked list
    def searchCSLL(self, value):
        if self.head is None:
            print("No any node to search.")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node does not exist!"
    
    # Delete in circular singly linked list
    def deleteNode(self, location):
        if self.head is None:
            print('No any node exists to delete!')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                else:
                    # If more than one element
                    # Make head ref to next node
                    # Then, make last node ref to second node
                    # Finally, garbage collector delete first node
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                else:
                    tempNode = self.head
                    while tempNode:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = self.head
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                delNode = tempNode.next
                tempNode.next = delNode.next

    # Delete entire circular singly linked list
    # Make 3 reference to null 
    def deleteEntireCLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None

circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(-1)

circularSLL.insertInCSLL(0, 0)
circularSLL.insertInCSLL(1, 0)
circularSLL.insertInCSLL(2, 0)

circularSLL.insertInCSLL(10, -1)
circularSLL.insertInCSLL(15, -1)

circularSLL.insertInCSLL(20, 3)
circularSLL.insertInCSLL(25, 4)
print([node.value for node in circularSLL])
# circularSLL.traversalCLL()
# print(circularSLL.searchCSLL(2))
# print(circularSLL.searchCSLL(4))
circularSLL.deleteNode(0)
circularSLL.deleteNode(-1)
circularSLL.deleteNode(2)
print([node.value for node in circularSLL])

circularSLL.deleteEntireCLL()
print([node.value for node in circularSLL])
