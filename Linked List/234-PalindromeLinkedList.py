class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        if not head.next:
            return True
        
        #finding the mid of list using slow and fast pointers
        slow = fast = head
        if not fast.next.next:
            return head.val == head.next.val
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reversing the second half of the list
        prev = None
        curr = slow
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head2 = prev
        head1 = head

        #checking if both the lists are same
        while head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next

        return True
    
#Time Complexity - O(n)
#Space Complexity - O(1)