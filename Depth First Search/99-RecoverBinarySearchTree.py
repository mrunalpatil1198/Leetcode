class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root) -> None:
        
        prev = None
        first = middle = last = None

        #inorder traversal
        def inorder(node):
            nonlocal prev, first, middle, last
            if not node:
                return
            inorder(node.left)
            #found a misplaced node value
            if prev and prev.val > node.val:
                if not first:
                    #prev and curr node might be swapped
                    first = prev
                    middle = node
                else:
                    #curr node is swapped with first
                    last = node
            prev = node
            inorder(node.right)
        
        inorder(root)

        #recovring the tree
        if not last:
            first.val, middle.val = middle.val, first.val
        else:
            first.val, last.val = last.val, first.val
        
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1, TreeNode(3, None, TreeNode(2)))
    s.recoverTree(root)
    print(root.val, root.left.val, root.left.right.val)

#Time Complexity - O(n)
#Space Complexity - O(1) - not considering recursion stack
