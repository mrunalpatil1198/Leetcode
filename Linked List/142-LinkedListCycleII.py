class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Solution:
    def detectCycle(self, head):
        if not head:
            return None
        slow = head
        fast = head

        #moving ahead slow by one node and fast by two nodes
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

            #breaking if they meet
            if(slow == fast):
                break
        
        if not fast or not fast.next:
            return None
        
        #finding out where the cycle begins by resetting slow to head and moving slow and fast one node at a time till they meet
        slow = head
        while(fast != slow):
            slow = slow.next
            fast = fast.next
        
        return slow
    
if __name__ == '__main__':
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = head.next
    s = Solution()
    intersection = s.detectCycle(head)
    print(intersection.val)

#Time Complexity - O(n)
#Space Complexity - O(1)