'''
Question: https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, pos is used to denote the 
index of the node that tail's next pointer is connected to. Note that pos is not passed 
as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

=> => =>
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to 
the 1st node (0-indexed).

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.


Follow up: Can you solve it using O(1) (i.e. constant) memory?


'''

# Time: O(n); Space: O(1)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Idea : Place some new unique value to current node value
        # if that value again comes then it has cycle
        # Time: O(n); Space: O(1)
        temp = head
        while temp:
            if temp.val == float('-inf'):
                return True
            
            temp.val = float('-inf')
            temp = temp.next
        return False
            

