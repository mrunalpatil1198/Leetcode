class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        #both lie in the same subtree rooted at root
        if root == p or root == q:
            return root
        
        #traversing left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        #returning root if p and q found
        if left and right:
            return root
        
        #both lie in one subtree rooted at either left or right
        return left or right
    
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    p = root.left = TreeNode(7)
    q = root.right = TreeNode(3)
    print(s.lowestCommonAncestor(root, p, q).val)

#Time Complexity - O(n)
#Space Complexity - O(1) - not considering recursion stack space