class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

class Solution:
    def preorderTraversal(self, root):
        result = []
        def traverse(root):
            if(root == None): 
                return
            #adding root to result
            result.append(root.val) 
            #traversing the left subtree
            traverse(root.left) 
            #traversing the right subtree
            traverse(root.right) 
        traverse(root)
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    s = Solution()
    print(s.preorderTraversal(root))


# Time Complexity -> O(n) -> T(n) = 2(T/2) + 1
# Space Complexity -> O(n) 