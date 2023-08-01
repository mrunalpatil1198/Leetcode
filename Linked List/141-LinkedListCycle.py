class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head):
        if not head:
            return None
        slow = head
        fast = head

        #moving slow pointer one node ahead and fast two nodes ahead
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

            #checking if cycle exists
            if slow == fast:
                return True
        return False
    
if __name__ == '__main__':
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = head
    s = Solution()
    print(s.hasCycle(head))

#Time Complexity - O(n)
#Space Complexity - O(1)
