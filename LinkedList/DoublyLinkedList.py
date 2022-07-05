
from sqlalchemy import null


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    # Creation of doubly linkedlist
    def createDoublyLL(self, value):
        newNode = Node(value)
        newNode.prev = None
        newNode.next = None
        self.head = newNode
        self.tail = newNode
        return "Creation of Doubly Linked List successful."
    
    # Insertion in Doubly Linked List
    def insertInDoublyLL(self, value, location):
        if self.head is None:
            print("First create a Doubly Linked List, called createDoublyLL() method.")
            return
        newNode = Node(value)
        if location == 0: # Time: O(1); Space: O(1)
            # insert at the beginning
            # 1. Create a newNode
            # 2. Make newNode prev ref to Null
            # 3. Make newNode.next to FirstNode
            # 4. Update FistNode.prev ref to newNode
            # 5. Update head ref to newNode.
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

        
        elif location == -1: # Time: O(1); Space: O(1)
            # Insert newNode at last of DoublyLL
            # 1. Create a newNode with a given value.
            # 2. Make newNode.next to null
            # 3. Make newNode.prev to lastNode
            # 4. Update lastNode.next to newNode
            # 5. Update tail to newNode
            newNode.next = None
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        
        else:
            # Insert newNode at specified location -> Time: O(n); Space: O(1)
            # 1. Creation of newNOde
            # 2. Traverse DoubleLL until index < location -1
            # 3. Make newNode.next = prevNode.next
            # 4. Update prevNode.next to newNode
            # 5. Update nextNode.prev = newNode
            # 6. Make newNode.prev = prevNode
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            newNode.next = nextNode
            tempNode.next = newNode
            newNode.prev = tempNode
            nextNode.prev = newNode
            
    # Traversal Method in DoublyLL -> Time: O(n); Space: O(1)
    def traverseDoublyLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    # Reverse Traversal Method in Doubly Linked List -> Time: O(n); Space: O(1)
    def reverseTraverseDoublyLL(self):
        if self.head is None:
            print("There is not any element to traverse.")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
    
    # Search Method in Doubly Linked List -> Time: O(n); Space: O(1)
    def searchElementDLL(self, value):
        if self.head is None:
            return "There is not any element in the Linked List to search."
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                tempNode = tempNode.next
            return "The node value does not exist in the linked list"

    # Deletion of node in Doubly Linked List
    def deleteElementDLL(self, location): # Time: O(n); Space: O(1)
        if self.head is None:
            return "No any node to delete in List."
        else:
            # Delete at the beginning of list -> Time: O(1); Space: O(1)
            if location == 0:
                # Case 1: if there is only one node
                # Update head and tail ref to null
                if self.head == self.tail:
                    self.head, self.tail = None, None
                else:
                    # Case 2: more than one node 
                        # 1. Update head to second node
                        # 2. Updare secondNode.prev to null
                    self.head = self.head.next
                    self.head.prev = None
            
            # Delete from the last of List -> Time: O(1); Space: O(1)
            elif location == -1:
                # Case 1: If there is only one element
                # Update head and tail ref to null
                if self.head == self.tail:
                    self.head, self.tail = None, None
                else:
                    # Case 2: more than one node
                        # 1. Update prevNode.next to null
                        # 2. Update tail to prevNode
                    prevNode = self.tail.prev
                    prevNode.next = None
                    self.tail = prevNode
            
            # Delete from the given location -> Time: O(n); Space: O(1)
            else:
                # 1. Traverse untill before given location
                # Update prevNode.next to nextNode
                # Update nextNode.prev to prevNode
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                
                delNode = tempNode.next
                nextNode = delNode.next
                tempNode.next = nextNode
                nextNode.prev = tempNode

    # Delete Entire Double Linked List
    def deleteEntireDoubleLL(self):  # -> Time: O(n); Space: O(1)
        # Steps:
        # 1. Traverse through list and make all node prev to null
        # 2. Finally Update head and tail ref to null
        # 3. By that Garbage collector delete the entire list where there is no
        #    connection in both ways
        node = self.head
        while node:
            node.prev = None
            node = node.next
        self.head = None
        self.tail = None

doublyLL = DoublyLinkedList()
doublyLL.createDoublyLL(1)

doublyLL.insertInDoublyLL(2, 0)
doublyLL.insertInDoublyLL(5, -1)
doublyLL.insertInDoublyLL(7, 1)
doublyLL.insertInDoublyLL(4, -1)
doublyLL.insertInDoublyLL(8, 2)
print([node.value for node in doublyLL])
# doublyLL.traverseDoublyLL()
# print("#######################")
# doublyLL.reverseTraverseDoublyLL()
# print("###########################")
# print(doublyLL.searchElementDLL(5))
doublyLL.deleteElementDLL(0)
doublyLL.deleteElementDLL(-1)
doublyLL.deleteElementDLL(2)
print([node.value for node in doublyLL])

doublyLL.deleteEntireDoubleLL()
print([node.value for node in doublyLL])


