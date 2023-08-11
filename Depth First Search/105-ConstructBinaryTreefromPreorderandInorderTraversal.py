from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]):
        val_to_inorder_index = {inorder[i] : i for i in range(len(inorder))}
        preorder = deque(preorder)

        def build(start, end):
            if not preorder or start < 0 or end >= len(inorder):
                return None
            #getting curr root
            root_val = preorder[0]
            inorder_index = val_to_inorder_index[root_val]
            if inorder_index < start or inorder_index > end:
                return None
            root = TreeNode(preorder.popleft())
            #building left subtree
            root.left = build(start, inorder_index-1)
            #building right subtree
            root.right = build(inorder_index+1, end)
            return root

        return build(0, len(inorder)-1)
    
if __name__ == '__main__':
    s = Solution()
    root = s.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])

#Time Complexity - O(n) 
#Space Complexity - O(1) - not considering recursive stack space
    
