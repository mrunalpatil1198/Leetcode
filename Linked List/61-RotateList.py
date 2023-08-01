class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Solution:
    def rotateRight(self, head, k):

        if not head or k == 0:
            return None
        
        temp = head
        length = 1

        #calculating length of the list
        while(temp.next):
            length += 1
            temp = temp.next
        end = temp

        #checking exactly how many places we need to rotate based on length
        if k > length:
            k = k % length
        if k == length or length == 1 or k == 0:
            return head
        
        #moving pointer k places forward
        temp = head
        for i in range(length - k - 1):
            temp = temp.next
        
        #updating head and end of the list
        new_head = temp.next
        temp.next = None
        end.next = head
        head = new_head

        return head
    
if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    s = Solution()
    head = s.rotateRight(head, 2)
    while(head):
        print(head.val)
        head = head.next


#Time Complexity - O(n)
#Space Complexity - O(1)