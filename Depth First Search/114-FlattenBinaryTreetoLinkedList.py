class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root) -> None:
        curr = None

        def traverse(root):
            if root is None:
                return
        
            left, right = root.left, root.right
            nonlocal curr
            if curr:
                #setting left child as None and right child as root
                curr.left = None
                curr.right = root
                curr = curr.right
            else:
                curr = root
                curr.left = None

            #traversing left subtree
            traverse(left)
            #traversing right subtree
            traverse(right)

        traverse(root)
        return curr
            
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    s = Solution()
    s.flatten(root)

    while(root):
        print(root.val)
        root = root.right

#Time Complexity - O(n)
#Space Complexity - O(1) - not considering recursion stack space