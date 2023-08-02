from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

        #checking if we have atleast k nodes left
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next

        prev = None
        curr = head
        #reversing those k nodes
        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        #setting next of curr head to the head returned by next k nodes reversal
        head.next = self.reverseKGroup(curr, k)

        #returning new head
        return prev
    
if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    reversed = s.reverseKGroup(head, 2)
    while reversed:
        print(reversed.val)
        reversed = reversed.next

#Time Complexity - O(n)
#Space Complexity - O(1) - not considering recursion stack