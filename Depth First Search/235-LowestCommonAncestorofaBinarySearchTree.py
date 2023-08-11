class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        smaller = min(p.val, q.val)
        bigger = max(p.val, q.val)
        if not root:
            return None
        if root.val >= smaller and root.val <= bigger:
            #smaller lies in left subtree and bigger in right subtree hence, root is the common ancestor
            return root
        if root.val < smaller:
            #traversing right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            #traversing left subtree
            return self.lowestCommonAncestor(root.left, p, q)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(6)
    p = root.left = TreeNode(5)
    q = root.right = TreeNode(8)
    print(s.lowestCommonAncestor(root, p, q).val)

#Time Complexity - O(h) where h = height of the tree
#Space Complexity - O(1) - not considering recursion stack space