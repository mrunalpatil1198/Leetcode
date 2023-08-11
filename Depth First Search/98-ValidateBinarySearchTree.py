class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        #variable to store prev node val in inorder traversal
        prev = float('-inf')

        #inorder traversal on root
        def inorder(node):
            if not node:
                return True
            nonlocal prev
            #traversing left subtree and returning false if inorder traversal is not sorted
            if not (inorder(node.left) and prev < node.val):
                return False
            prev = node.val
            #traversing right subtree
            return inorder(node.right)

        return inorder(root)
    
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(s.isValidBST(root))
            
#Time Complexity - O(n)
#Space Complexity - O(1) - not considering recursion stack space