'''
Question: https://leetcode.com/problems/merge-two-sorted-lists/
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
=> => => => =>
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Input: list1 = [], list2 = []
Output: []

Idea Explained at: https://leetcode.com/problems/merge-two-sorted-lists/discuss/2253040/O(n)-O(1)Python-Merging-Explained-with-detail-output

'''
# Solution: Time: O(n); Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode()
        head = dummy
        # Take out all the values of both linked list
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
            # print(f"head: {head}")
            # print(f"Dummy: {dummy}")            
        if list1 or list2:
            head.next = list1 if list1 else list2
        
        # print("Finally")
        # print(f"head: {head}")
        # print(f"Dummy: {dummy}")    
        return dummy.next
        