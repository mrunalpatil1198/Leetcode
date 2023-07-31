from queue import PriorityQueue

class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        q = PriorityQueue()
        dummy = ListNode(0)
        end = dummy

        #adding heads and head values of all lists into priority queue
        for list in lists:
            if list:
                q.put((list.val, list))
        
        while not q.empty():
            #getting the list head with minimum value
            value, temp = q.get()

            #adding next node of chosen list
            if temp.next:
                q.put((temp.next.val, temp.next))

            #moving list pointers forward
            end.next = ListNode(value)
            end = end.next
        
        return dummy.next
    
if __name__ == '__main__':
    s = Solution()
    list1 = ListNode(3)
    list1.next = ListNode(5)
    list1.next.next = ListNode(6)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(7)

    list3 = ListNode(0)
    list3.next = ListNode(2)
    list3.next.next = ListNode(9)

    lists = []
    lists.append(list1)
    lists.append(list2)
    lists.append(list3)

    head = s.mergeKLists(lists)
    while(head):
        print(head.val)
        head = head.next

#Time Complexity - O(k*n)
#Space Complexity - O(k)