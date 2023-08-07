from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum = 0
        def dfs(node, s):
            if not node:
                return
            #appending curr val
            s += str(node.val)
            #if reached a leaf node
            if not node.left and not node.right:
                nonlocal sum
                #updating sum
                sum += int(s)
            #traversig left subtree
            dfs(node.left, s)
            #traversing right subtree
            dfs(node.right, s)
        dfs(root,'')
        return sum

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(s.sumNumbers(root))

#Time Complexity - O(n)
#Space Complexity - O(1) - not considering recursion stack
