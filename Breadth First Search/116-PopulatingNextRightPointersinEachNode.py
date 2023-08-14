from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if not root:
            return None
        
        q = deque()
        q.append(root)

        #bfs
        while q:
            size = len(q)
            prev = None
            #traversing curr level
            for _ in range(size):
                curr = q.popleft()
                curr.next = prev
                prev = curr
                #traversing right subtree first as we are storing right node as prev
                if curr.right:
                    q.append(curr.right)
                #traversing left subtree
                if curr.left:
                    q.append(curr.left)

        return root
    
if __name__ == '__main__':
    s = Solution()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    s.connect(root)

#Time Complexity - O(n)
#Space Complexity - O(n)