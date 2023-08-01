class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverse(self, head):

        #initializing the pointers
        curr = head
        prev = None
        next = None

        while(curr):
            #saving the next node
            next = curr.next

            #next of current should point towards prev node
            curr.next = prev

            #prev should point towards curr
            prev = curr

            #curr should be moved one node right for next iteration
            curr = next

        #prev is the new head
        return prev
    
    def display(self, head):
        while(head):
            print(head.val)
            head = head.next
    
if __name__ == '__main__':
    s = Solution()
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    s.display(head)
    head = s.reverse(head)
    s.display(head)

#Time Complexity - O(n)
#Space Complexity - O(1)