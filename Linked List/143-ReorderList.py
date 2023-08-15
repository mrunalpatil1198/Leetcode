class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head) -> None:
        if not head:
            return head
        
        #finding the mid of list using lsow and fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        #reversing the second half of the list
        prev = None
        while head2:
            next = head2.next
            head2.next = prev
            prev = head2
            head2 = next
        
        #alternately linking nodes from the first half and the reversed second half
        first = head
        second = prev
        while second:
            next1, next2 = first.next, second.next
            first.next = second
            second.next = next1
            first, second = next1, next2

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    s.reorderList(head)
    while head:
        print(head.val)
        head = head.next

#Time Complexity - O(n)
#Space Complexity - O(1)