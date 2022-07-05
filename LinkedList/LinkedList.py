

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self) -> str:
        values = [str(x.value) for x in self]
        return ' -> '.join(values)
    
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    
    # insert in Linked List
    def insert_element(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            # insert at first : Time: O(1)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            # insert at last: Time: O(1)
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            # insert at nth postion: Time: O(n)
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def delete_element(self, location):
        if self.head is None:
            print("Linked List does not exist")

        else:
            if location == 0:
                # if have only one node
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    temp = self.head
                    self.head = temp.next
                    temp = None

            # delete from last position : Time: O(n)
            elif location == -1:
                # #1. if we have only one node
                if(self.head == self.tail):
                    self.head = None
                    self.tail = None
                else:
                    # 2. Else, traverse to the second last
                    #   element of the list
                    tempNode = self.head
                    while(tempNode is not None):
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    # 3. Change the next of the second
                    #   last node to null and delete the
                    #   last node
                    tempNode.next = None
                    self.tail = tempNode

            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                delNode = tempNode.next
                tempNode.next = delNode.next
    
    # Delete whole SLL
    # Time: O(1) ; Space: O(1)
    def deleteAllSLL(self):
        # Idea is to make reference to head and tail to null
        # Garbage collector then destroy all node
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None


singlyLinkedList = SLinkedList()

singlyLinkedList.insert_element(0, 0)
singlyLinkedList.insert_element(1, 0)
singlyLinkedList.insert_element(2, 0)

singlyLinkedList.insert_element(10, -1)
singlyLinkedList.insert_element(15, -1)

singlyLinkedList.insert_element(20, 3)
singlyLinkedList.insert_element(25, 4)

print(singlyLinkedList)

singlyLinkedList.delete_element(4)
singlyLinkedList.delete_element(0)
singlyLinkedList.delete_element(-1)
print(singlyLinkedList)

singlyLinkedList.deleteAllSLL()
print(singlyLinkedList)
