from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root):
        if not root:
            return []
        
        result = []
        q = deque()
        q.append(root)

        #bfs
        while q:
            size = len(q)
            temp = float('-inf')
            for _ in range(size):
                curr = q.popleft()
                #updating max for curr level
                temp = max(temp, curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            #adding max of curr level to result
            result.append(temp)
        
        return result
    
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3, TreeNode(5), TreeNode(3))
    root.right = TreeNode(2, None, TreeNode(9))
    print(s.largestValues(root))

#Time Complexity - O(n)
#Space Complexity - O(n)