class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root) -> bool:

        def dfs(node):
            if not node:
                return 0
            
            #traversing left and right subtree
            left_ht = dfs(node.left)
            right_ht = dfs(node.right)

            #checking if it is balanced on lower level and curr level
            if left_ht < 0 or right_ht < 0 or abs(left_ht-right_ht) > 1: 
                return -1
            
            #incrementing height by 1 at every level
            return max(left_ht, right_ht) + 1
        
        result = dfs(root)
        return result >= 0
    
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    print(s.isBalanced(root))

#Time Complexity - O(n)
#Space Complexity - O(1) - not considering recursive stack space