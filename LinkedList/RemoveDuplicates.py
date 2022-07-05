from LinkedList2 import LinkedList

# Remove duplicates elemnent from linked list
def removeDuplicates(ll):
    if ll.head is None:
        return
    else:
        curNode = ll.head
        visitedNode = set([curNode.value])
        while curNode.next:
            if curNode.next.value in visitedNode:
                curNode.next = curNode.next.next
            else:
                visitedNode.add(curNode.next.value)
                curNode = curNode.next
        return ll

# Implement an algorithm to find the nth from the last element of a singly linked list



customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
removeDuplicates(customLL)
print(customLL)
    