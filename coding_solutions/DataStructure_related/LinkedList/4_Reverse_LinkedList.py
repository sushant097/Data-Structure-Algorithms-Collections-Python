'''
Question: https://leetcode.com/problems/reverse-linked-list/
Given the head of a singly linked list, reverse the list, and return the reversed list.

=> => => =>
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Appraoch 1: Iterative approach -> Time: O(n); Space: O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative solution
        # Time: O(n), Space: O(n)
        
        if not head:
            return head

        if not head.next:
            return head
        # Get the values of linked List
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        # Create the new linkedlist with the values 
        # Where the values are in reverse order
        for i in range(len(values)):
            if i == 0:
                left = ListNode(values[i])
            else:
                left = ListNode(values[i], left)
            # print(f"{left}")
        return left
        

# Approach : Recursive with Queue Data Structure -> Time: O(n); Space: O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive Solution : Queue Data Structure
        # Time: O(n); Space: O(n)
        queue = []
        
        self.process(head, queue)
        
        return head
    
    def process(self, head: Optional[ListNode], queue) -> None:
        
        if not head:
            return 
        queue.append(head.val)
        self.process(head.next, queue)
        # after recursive all the values are in queue
        # These values are in descending order
        # Just update head value with values of queue
        head.val = queue.pop(0)
        
            
