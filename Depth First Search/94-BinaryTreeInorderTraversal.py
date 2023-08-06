class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

class Solution:
    def inorderTraversal(self, root):
        result = []
        def traverse(root):
            if(root == None): 
                return
            #traverse the left subtree
            traverse(root.left) 
            #add root to result
            result.append(root.val)
            #traverse the right subtree 
            traverse(root.right) 
        traverse(root)
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    s = Solution()
    print(s.inorderTraversal(root))


# Time Complexity -> O(n) -> T(n) = 2(T/2) + 1
# Space Complexity -> O(1) - not considering recursive stack space 