class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head

        #moving fast n places from head
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next
        
        #when fast reaches the end, slow would be at nth node from end
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        #removing nth node
        slow.next = slow.next.next
        return head
    
if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    s = Solution()
    head = s.removeNthFromEnd(head, 5)
    while(head):
        print(head.val)
        head = head.next

#Time Complexity - O(n)
#Space Complexity - O(1)
