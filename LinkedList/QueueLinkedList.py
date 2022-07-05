

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
    
    def __str__(self) -> str:
        return str(self.value)
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
        
    
class Queue:
    def __init__(self) -> None:
        self.linkedList = LinkedList()

    def __str__(self) -> str:
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
    
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue Underflow! No any element."
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode

    def peek(self):
        if self.isEmpty():
            return "Queue Underflow! No any element."
        else:
            return self.linkedList.head

    
    def deleteQueue(self):
        self.linkedList.head = None
        self.linkedList.tail = None

    
custQueue = Queue()
custQueue.enqueue(10)
custQueue.enqueue(11)
custQueue.enqueue(12)
print(custQueue)
print(custQueue.dequeue())
print(custQueue)
print(custQueue.peek())
print(custQueue)