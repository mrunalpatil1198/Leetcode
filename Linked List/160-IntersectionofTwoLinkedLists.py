class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        while(True):
            if headA == headB:
                return headA
            #running pointers through both the lists
            headA = headA.next if headA else headB
            headB = headB.next if headB else headA
        return None
    
if __name__ == '__main__':
    head = ListNode(0)
    head.next = ListNode()

#Time Complexity - O(m+n)
#Space Complexity - O(1)