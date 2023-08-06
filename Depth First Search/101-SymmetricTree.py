class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root) -> bool:

        if not root:
            return root

        def isSame(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            
            #traversing left subtree of left child and right subtree of right child and also right subtree of left child and left subtree of right child
            return isSame(left.left, right.right) and isSame(left.right, right.left)

        return isSame(root.left, root.right)
    
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    s = Solution()
    print(s.isSymmetric(root))

#Time Complexity - O(n)
#Space Complexity - O(1) - not considering recursion stack