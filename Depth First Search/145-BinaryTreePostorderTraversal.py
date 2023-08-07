class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

class Solution:
    def postorderTraversal(self, root):
        result = []
        def traverse(root):
            if(root == None): 
                return
            #traversing the left subtree
            traverse(root.left)
            #traversing the right subtree
            traverse(root.right)
            #adding root to result
            result.append(root.val)
        traverse(root)
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    s = Solution()
    print(s.postorderTraversal(root))


# Time Complexity -> O(n) -> T(n) = 2(T/2) + 1
# Space Complexity -> O(n) 