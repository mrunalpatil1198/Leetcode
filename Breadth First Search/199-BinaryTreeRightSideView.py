from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        if not root:
            return root
        q = deque()
        q.append(root)
        result = []

        #bfs
        while q:
            #adding last node of curr level into result
            result.append(q[-1].val)
            size = len(q)
            while size > 0:
                temp = q.popleft()
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                size -= 1
        
        return result
    
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2, None, TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(4))
    print(s.rightSideView(root))
        
#Time Complexity - O(n)
#Space Complexity - O(n)