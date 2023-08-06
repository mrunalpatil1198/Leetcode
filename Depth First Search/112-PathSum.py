class TreeNode:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value

class Solution:

    def pathSum(self, root, target):
        if root is None:
            return False
        
        target -= root.value
        if root.left is None and root.right is None:
            return target == 0
        
        #traversing left subtree and right subtree
        return self.pathSum(root.left, target) or self.pathSum(root.right, target)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    s = Solution()
    print(s.pathSum(root, 5))

#Time Complexity - O(n)
#Space Complexity - O(1) - not considering recursion stack space