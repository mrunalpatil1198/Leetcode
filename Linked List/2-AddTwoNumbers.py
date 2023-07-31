class ListNode:
    def __init__(self, val = 0) -> None:
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):

        head = ListNode()
        current = head
        carry = 0

        while (l1 != None or l2 != None or carry != 0):
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0

            #summing list1, list2 and curr carry
            total = l1_value + l2_value + carry

            #adding last digit of the sum to result list
            current.next = ListNode(total % 10)
            carry = total // 10
            
            #moving list pointers forward
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next

        return head.next
    
if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s = Solution()
    head = s.addTwoNumbers(l1, l2)
    while(head):
        print(head.val)
        head = head.next

#Time Complexity - O(n)
#Space Complexity - O(1) - ignoring space required for the result