class TreeNode:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value

class Solution:
    def kthSmallest(self, root, k) -> int:

        #iterative inorder traversal
        def inorder(node):
            stack = []
            curr = root
            while True:
                if curr is not None:
                    #traversing left subtree
                    stack.append(curr)
                    curr = curr.left
                elif(stack):
                    #getting the kth element - root
                    curr = stack.pop()
                    nonlocal k
                    k -= 1
                    if k == 0:
                        return curr.value
                    #traversing right subtree
                    curr = curr.right
                else:
                    break
        
        return inorder(root)
    
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)

    s = Solution()
    print(s.kthSmallest(root, 2))

#Time Complexity - O(n)
#Space Complexity - O(n)