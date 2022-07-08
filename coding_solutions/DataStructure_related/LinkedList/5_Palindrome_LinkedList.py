'''
Question: https://leetcode.com/problems/palindrome-linked-list/
Given the head of a singly linked list, return true if it is a palindrome.

=> => => =>
Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false

Follow up: Could you do it in O(n) time and O(1) space?

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution: Time: O(n); Space: O(n)
# First we get all the values of LinkedList
# Check whether that values is equal to reverse of this
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        # print(values)
        # Check if the values == reverse of that
        i = 0
        j = len(values) - 1
        while i < j:
            if values[i] != values[j]:
                return False
            i += 1
            j -= 1
        return True


"Follow up: Could you do it in O(n) time and O(1) space?"
# Solution : Time: O(n); Space: O(1)
# We will utilize two algorithm methods:
# Floyd's Tortoise & Hare Algorithm aka Fast and Slow Pointers + Linked List Reversal
# Time is O(n) because in the worst case we are just traversing through the entire linked list in a single iteration time.
# Space is O(1) because we aren't saving the entire input/linked list anywhere during our algorithm, so there is no scaling memory. 
# Only we keep track of variables and pointers.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True

        slow = head
        fast = head

        # We use slow and fast pointer algorithm to get the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half head ; Reverse in between [slow, tail]
        secondHalfEnd = self.reverse(slow)

        # check the reverse second half and first half
        # so use two pointers
        # Pointer1 is in starting and pointer2 is in middle
        pointer1 = head
        pointer2 = secondHalfEnd
        validPalindrome = True

        while pointer1 and pointer2:
            if pointer1.val != pointer2.val:
                validPalindrome = False
                break
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        # Reverse the second half of the linked list back to normal
        self.reverse(secondHalfEnd)
        return validPalindrome

    def reverse(self, head):
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
