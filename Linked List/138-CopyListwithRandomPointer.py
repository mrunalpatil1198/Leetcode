class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        #creating a dictionary to maintain all the clones
        clones = {None:None}
        curr = head

        #creating copies of all nodes of given ll and adding into the dictionary
        while curr:
            clones[curr] = Node(curr.val)
            curr = curr.next
        curr = head

        #setting the next and random pointer for all the copies created
        while curr:
            clone = clones[curr]
            clone.next = clones[curr.next]
            clone.random = clones[curr.random]
            curr = curr.next
        return clones[head]
    
    
#Time Complexity - O(n)
#Space Complexity - O(n)