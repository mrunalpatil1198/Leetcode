class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Solution:
    def removeElements(self, head, val):
        # if not head:
        #     return None
        # dummy = ListNode(0)
        # prev = dummy
        # temp = head
        # while(temp):
        #     if temp.val != val:
        #         prev.next = temp
        #         prev = prev.next
        #     temp = temp.next
        # return dummy.next
        if head is None:
            return head

        #removing the first nodes with value = val
        while(head and head.val == val):
            head = head.next

        temp = head
        while(temp and temp.next):
            #moving next pointer of the curr node to next of next if curr.next has value = val
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                #moving pointer right side
                temp = temp.next
        return head
    
if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(6)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next.next = ListNode(6)
    s = Solution()
    head = s.removeElements(head, 6)
    while(head):
        print(head.val)
        head = head.next

#Time Complexity - O(n)
#Space Complexity - O(1)

